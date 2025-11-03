from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import json
import io
from contextlib import redirect_stdout, redirect_stderr
from .models import Category, Question, Choice, TestCase
from .serializers import CategorySerializer, QuestionSerializer, ChoiceSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        queryset = Question.objects.all()
        question_type = self.request.query_params.get('type', None)
        difficulty = self.request.query_params.get('difficulty', None)
        category = self.request.query_params.get('category', None)
        
        if question_type:
            queryset = queryset.filter(question_type=question_type)
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)
        if category:
            queryset = queryset.filter(category_id=category)
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def random(self, request):
        question_type = request.query_params.get('type', None)
        count = request.query_params.get('count', None)
        difficulty = request.query_params.get('difficulty', None)
        queryset = Question.objects.all()
        
        if question_type:
            queryset = queryset.filter(question_type=question_type)
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)
        
        if count:
            try:
                count = int(count)
                questions = list(queryset.order_by('?')[:count])
                if questions:
                    serializer = self.get_serializer(questions, many=True)
                    return Response(serializer.data)
                return Response({'error': 'No questions found'}, status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                return Response({'error': 'Invalid count parameter'}, status=status.HTTP_400_BAD_REQUEST)
        
        question = queryset.order_by('?').first()
        if question:
            serializer = self.get_serializer(question)
            return Response(serializer.data)
        return Response({'error': 'No questions found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def check_answer(self, request, pk=None):
        question = self.get_object()
        
        if question.question_type == 'multiple_choice':
            choice_id = request.data.get('choice_id')
            try:
                choice = Choice.objects.get(id=choice_id, question=question)
                if choice.is_correct:
                    return Response({
                        'correct': True,
                        'message': 'Correct! 🎉'
                    })

                # On incorrect answers, include the correct choice(s) info so frontend can show it
                correct_choices = Choice.objects.filter(question=question, is_correct=True)
                correct_info = [
                    {'id': c.id, 'text': c.text} for c in correct_choices
                ]

                return Response({
                    'correct': False,
                    'message': 'Wrong answer, try again! ❌',
                    'correct_choices': correct_info
                })
            except Choice.DoesNotExist:
                return Response({
                    'error': 'Choice not found'
                }, status=status.HTTP_400_BAD_REQUEST)
        
        elif question.question_type == 'coding':
            user_code = request.data.get('code', '')
            if not user_code:
                return Response({
                    'error': 'Code is required'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Get all test cases (including hidden ones for validation)
            test_cases = TestCase.objects.filter(question=question)
            
            results = []
            all_passed = True
            
            for test_case in test_cases:
                test_result = self._run_test_case(user_code, test_case)
                results.append(test_result)
                if not test_result['passed']:
                    all_passed = False
                    # Stop on first failure if it's not hidden
                    if not test_case.is_hidden:
                        break
            
            # Filter visible test results
            visible_results = []
            test_cases_list = list(test_cases)
            for i, r in enumerate(results):
                if i < len(test_cases_list) and not test_cases_list[i].is_hidden:
                    visible_results.append(r)
            
            return Response({
                'correct': all_passed,
                'message': 'All test cases passed! 🎉' if all_passed else 'Some test cases failed. Try again! ❌',
                'test_results': visible_results
            })
        
        return Response({
            'error': 'Invalid question type'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def _run_test_case(self, user_code, test_case):
        """Execute user code against a test case"""
        try:
            # Parse input and expected output
            input_data = test_case.get_input()
            expected_output = test_case.get_expected_output()
            
            # Create a safe execution environment
            exec_globals = {'__builtins__': __builtins__}
            exec_locals = {}
            
            # Prepare input variables
            if isinstance(input_data, dict):
                exec_globals.update(input_data)
            else:
                exec_globals['input_data'] = input_data
            
            # Capture output
            output_buffer = io.StringIO()
            error_buffer = io.StringIO()
            
            try:
                with redirect_stdout(output_buffer), redirect_stderr(error_buffer):
                    # Execute user code
                    exec(user_code, exec_globals, exec_locals)
                    
                    # Update locals with any new variables from execution
                    exec_locals.update(exec_globals)
                    
                    # Try to get result from common variable names or function calls
                    result = None
                    
                    # First, try common result variable names
                    for var_name in ['result', 'output', 'answer', 'solution']:
                        if var_name in exec_locals:
                            result = exec_locals[var_name]
                            break
                    
                    # If input_data is a dict, try calling a function with those parameters
                    if result is None and isinstance(input_data, dict):
                        # Look for function definitions
                        for key, value in exec_locals.items():
                            if callable(value) and not key.startswith('_'):
                                # Try calling the function with input_data as kwargs
                                try:
                                    result = value(**input_data)
                                    break
                                except:
                                    try:
                                        # Try as single argument if only one key
                                        if len(input_data) == 1:
                                            result = value(next(iter(input_data.values())))
                                            break
                                    except:
                                        pass
                    
                    # If no result variable, get stdout
                    if result is None:
                        stdout_value = output_buffer.getvalue().strip()
                        if stdout_value:
                            # Try to parse stdout as result
                            try:
                                # Try JSON first
                                result = json.loads(stdout_value)
                            except:
                                # Try as number
                                try:
                                    if '.' in stdout_value:
                                        result = float(stdout_value)
                                    else:
                                        result = int(stdout_value)
                                except:
                                    result = stdout_value
                    
                    # Normalize result for comparison
                    if result is not None:
                        # Try to convert to same type as expected
                        if isinstance(expected_output, (int, float)) and isinstance(result, str):
                            try:
                                if isinstance(expected_output, int):
                                    result = int(float(result))
                                elif isinstance(expected_output, float):
                                    result = float(result)
                            except:
                                pass
                        elif isinstance(expected_output, str) and not isinstance(result, str):
                            result = str(result)
                        elif isinstance(expected_output, (list, dict)) and not isinstance(result, type(expected_output)):
                            # Try to convert if types don't match
                            if isinstance(expected_output, list):
                                try:
                                    result = list(result) if result else []
                                except:
                                    pass
                    
                    # Compare results
                    passed = self._compare_results(result, expected_output)
                    error_msg = error_buffer.getvalue()
                    
                    # Get index more efficiently
                    test_cases_list = list(TestCase.objects.filter(question=test_case.question).order_by('id'))
                    test_index = next((i for i, tc in enumerate(test_cases_list) if tc.id == test_case.id), 0)
                    
                    return {
                        'passed': passed,
                        'input': input_data,
                        'expected': expected_output,
                        'got': result,
                        'error': error_msg if error_msg else None,
                        'index': test_index
                    }
                    
            except Exception as e:
                test_cases_list = list(TestCase.objects.filter(question=test_case.question).order_by('id'))
                test_index = next((i for i, tc in enumerate(test_cases_list) if tc.id == test_case.id), 0)
                
                return {
                    'passed': False,
                    'input': input_data,
                    'expected': expected_output,
                    'got': None,
                    'error': str(e),
                    'index': test_index
                }
                
        except Exception as e:
            return {
                'passed': False,
                'input': input_data if 'input_data' in locals() else None,
                'expected': expected_output if 'expected_output' in locals() else None,
                'got': None,
                'error': f'Test execution error: {str(e)}',
                'index': 0
            }
    
    def _compare_results(self, got, expected):
        """Compare results with tolerance for floating point and type differences"""
        if got is None and expected is None:
            return True
        if got is None or expected is None:
            return False
        
        # Exact match
        if got == expected:
            return True
        
        # Try type conversion
        try:
            if isinstance(expected, (int, float)) and isinstance(got, (str, int, float)):
                if isinstance(expected, int):
                    return int(float(str(got))) == expected
                elif isinstance(expected, float):
                    return abs(float(got) - expected) < 1e-9
        except:
            pass
        
        # List comparison (order-sensitive)
        if isinstance(expected, list) and isinstance(got, (list, tuple)):
            got_list = list(got) if isinstance(got, tuple) else got
            if len(got_list) != len(expected):
                return False
            return all(self._compare_results(g, e) for g, e in zip(got_list, expected))
        
        # Dict comparison
        if isinstance(expected, dict) and isinstance(got, dict):
            if set(got.keys()) != set(expected.keys()):
                return False
            return all(self._compare_results(got[key], expected[key]) for key in expected.keys())
        
        # String comparison (case-insensitive, strip whitespace)
        if isinstance(expected, str) and isinstance(got, str):
            return got.strip().lower() == expected.strip().lower()
        
        return False
