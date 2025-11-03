from rest_framework import serializers
from .models import Category, Question, Choice, TestCase

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct']

class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ['id', 'input_data', 'expected_output', 'is_hidden']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    test_cases = TestCaseSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'text', 'question_type', 'difficulty', 'choices', 
                  'starter_code', 'test_cases', 'created_at']
    
    def to_representation(self, instance):
        """Hide is_correct from choices and hide hidden test cases"""
        data = super().to_representation(instance)
        if instance.question_type == 'multiple_choice':
            # Hide is_correct for multiple choice questions
            for choice in data.get('choices', []):
                if 'is_correct' in choice:
                    del choice['is_correct']
        else:
            # Hide hidden test cases for coding questions
            data['test_cases'] = [
                tc for tc in data.get('test_cases', []) 
                if not tc.get('is_hidden', True)
            ]
        return data

class CategorySerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'questions_count']
    
    def get_questions_count(self, obj):
        return obj.questions.count()