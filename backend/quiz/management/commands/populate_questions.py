import json
from django.core.management.base import BaseCommand
from quiz.models import Category, Question, Choice, TestCase

class Command(BaseCommand):
    help = 'Populate database with Python questions'

    def handle(self, *args, **options):
        # Create or get Python category
        category, _ = Category.objects.get_or_create(
            name='Python',
            defaults={'description': 'Python programming questions covering basics to advanced topics'}
        )

        # Multiple Choice Questions
        mc_questions = [
            # Basics
            {
                'text': 'What is the output of: print(type(5/2))',
                'difficulty': 'easy',
                'choices': [
                    ('<class "int">', False),
                    ('<class "float">', True),
                    ('<class "str">', False),
                    ('<class "double">', False),
                ]
            },
            {
                'text': 'Which method is used to add an element to the end of a list?',
                'difficulty': 'easy',
                'choices': [
                    ('append()', True),
                    ('add()', False),
                    ('insert()', False),
                    ('push()', False),
                ]
            },
            {
                'text': 'What is the result of: [x*2 for x in range(5) if x % 2 == 0]',
                'difficulty': 'medium',
                'choices': [
                    ('[0, 4, 8]', True),
                    ('[0, 2, 4, 6, 8]', False),
                    ('[4, 8]', False),
                    ('[2, 4, 6, 8]', False),
                ]
            },
            {
                'text': 'What does the `pass` keyword do in Python?',
                'difficulty': 'easy',
                'choices': [
                    ('Skips the current iteration', False),
                    ('Does nothing, placeholder for empty code', True),
                    ('Exits the function', False),
                    ('Raises an exception', False),
                ]
            },
            {
                'text': 'What is the time complexity of accessing an element in a dictionary by key?',
                'difficulty': 'medium',
                'choices': [
                    ('O(n)', False),
                    ('O(log n)', False),
                    ('O(1)', True),
                    ('O(n log n)', False),
                ]
            },
            {
                'text': 'Which of the following is NOT a valid variable name in Python?',
                'difficulty': 'easy',
                'choices': [
                    ('_variable', False),
                    ('2variable', True),
                    ('variable_name', False),
                    ('VariableName', False),
                ]
            },
            {
                'text': 'What does `*args` represent in a function definition?',
                'difficulty': 'medium',
                'choices': [
                    ('A single argument', False),
                    ('Variable number of positional arguments', True),
                    ('Variable number of keyword arguments', False),
                    ('A required argument', False),
                ]
            },
            {
                'text': 'Which method is used to remove an item from a dictionary?',
                'difficulty': 'easy',
                'choices': [
                    ('remove()', False),
                    ('delete()', False),
                    ('pop()', True),
                    ('discard()', False),
                ]
            },
            {
                'text': 'What is the output of: bool([])',
                'difficulty': 'easy',
                'choices': [
                    ('True', False),
                    ('False', True),
                    ('Error', False),
                    ('None', False),
                ]
            },
            {
                'text': 'What is the purpose of `__init__` method in a class?',
                'difficulty': 'easy',
                'choices': [
                    ('To destroy the object', False),
                    ('To initialize the object', True),
                    ('To convert to string', False),
                    ('To compare objects', False),
                ]
            },
            {
                'text': 'What is list comprehension syntax?',
                'difficulty': 'medium',
                'choices': [
                    ('[expression for item in iterable]', True),
                    ('(expression for item in iterable)', False),
                    ('{expression for item in iterable}', False),
                    ('expression for item in iterable', False),
                ]
            },
            {
                'text': 'What is the difference between `==` and `is` in Python?',
                'difficulty': 'medium',
                'choices': [
                    ('== compares values, is compares identities', True),
                    ('== compares identities, is compares values', False),
                    ('They are the same', False),
                    ('== is for strings, is is for numbers', False),
                ]
            },
            {
                'text': 'What does the `enumerate()` function return?',
                'difficulty': 'medium',
                'choices': [
                    ('A list of tuples', False),
                    ('An enumerate object with (index, value) pairs', True),
                    ('A dictionary', False),
                    ('A set', False),
                ]
            },
            {
                'text': 'What is a generator in Python?',
                'difficulty': 'medium',
                'choices': [
                    ('A function that returns a list', False),
                    ('A function that yields values one at a time', True),
                    ('A built-in data type', False),
                    ('A class method', False),
                ]
            },
            {
                'text': 'Which of these creates a shallow copy?',
                'difficulty': 'hard',
                'choices': [
                    ('copy.copy()', True),
                    ('copy.deepcopy()', False),
                    ('list()', False),
                    ('[:]', False),
                ]
            },
            # Additional Basics
            {
                'text': 'What is the output of: print(5 // 2)',
                'difficulty': 'easy',
                'choices': [
                    ('2.5', False),
                    ('2', True),
                    ('3', False),
                    ('2.0', False),
                ]
            },
            {
                'text': 'What is the output of: print(2 ** 3)',
                'difficulty': 'easy',
                'choices': [
                    ('6', False),
                    ('8', True),
                    ('9', False),
                    ('5', False),
                ]
            },
            {
                'text': 'What does `len()` return for an empty list?',
                'difficulty': 'easy',
                'choices': [
                    ('None', False),
                    ('0', True),
                    ('-1', False),
                    ('Error', False),
                ]
            },
            {
                'text': 'Which operator is used for exponentiation in Python?',
                'difficulty': 'easy',
                'choices': [
                    ('^', False),
                    ('**', True),
                    ('pow()', False),
                    ('exp()', False),
                ]
            },
            {
                'text': 'What is the output of: print("hello" * 3)',
                'difficulty': 'easy',
                'choices': [
                    ('hellohellohello', True),
                    ('hello3', False),
                    ('Error', False),
                    ('3hello', False),
                ]
            },
            # String Operations
            {
                'text': 'What method removes whitespace from both ends of a string?',
                'difficulty': 'easy',
                'choices': [
                    ('trim()', False),
                    ('strip()', True),
                    ('remove()', False),
                    ('clean()', False),
                ]
            },
            {
                'text': 'What does `"hello".upper()` return?',
                'difficulty': 'easy',
                'choices': [
                    ('HELLO', True),
                    ('hello', False),
                    ('Hello', False),
                    ('Error', False),
                ]
            },
            {
                'text': 'What is the output of: "Python".find("th")',
                'difficulty': 'medium',
                'choices': [
                    ('2', True),
                    ('3', False),
                    ('True', False),
                    ('-1', False),
                ]
            },
            {
                'text': 'What does `"hello,world".split(",")` return?',
                'difficulty': 'easy',
                'choices': [
                    ('["hello", "world"]', True),
                    ('"hello world"', False),
                    ('("hello", "world")', False),
                    ('Error', False),
                ]
            },
            {
                'text': 'What is the output of: print("abc" in "abcdef")',
                'difficulty': 'easy',
                'choices': [
                    ('True', True),
                    ('False', False),
                    ('1', False),
                    ('Error', False),
                ]
            },
            # List Operations
            {
                'text': 'What does `[1, 2, 3].pop()` return?',
                'difficulty': 'medium',
                'choices': [
                    ('3', True),
                    ('1', False),
                    ('[1, 2]', False),
                    ('None', False),
                ]
            },
            {
                'text': 'What is the output of: [1, 2, 3] + [4, 5]',
                'difficulty': 'easy',
                'choices': [
                    ('[1, 2, 3, 4, 5]', True),
                    ('[5, 7]', False),
                    ('Error', False),
                    ('[1, 2, 3][4, 5]', False),
                ]
            },
            {
                'text': 'What does `[1, 2, 3].extend([4, 5])` return?',
                'difficulty': 'medium',
                'choices': [
                    ('None (modifies list in place)', True),
                    ('[1, 2, 3, 4, 5]', False),
                    ('[4, 5]', False),
                    ('Error', False),
                ]
            },
            {
                'text': 'What is the output of: [x for x in range(5) if x % 2 == 0]',
                'difficulty': 'medium',
                'choices': [
                    ('[0, 2, 4]', True),
                    ('[1, 3]', False),
                    ('[0, 1, 2, 3, 4]', False),
                    ('[2, 4]', False),
                ]
            },
            {
                'text': 'What method is used to reverse a list in place?',
                'difficulty': 'medium',
                'choices': [
                    ('reverse()', True),
                    ('reversed()', False),
                    ('[::-1]', False),
                    ('invert()', False),
                ]
            },
            # Dictionary Operations
            {
                'text': 'What does `dict.get(key, default)` return if key is not found?',
                'difficulty': 'easy',
                'choices': [
                    ('The default value', True),
                    ('None', False),
                    ('KeyError', False),
                    ('False', False),
                ]
            },
            {
                'text': 'What is the output of: {"a": 1, "b": 2}.keys()',
                'difficulty': 'medium',
                'choices': [
                    ("dict_keys(['a', 'b'])", True),
                    ("['a', 'b']", False),
                    ("('a', 'b')", False),
                    ('Error', False),
                ]
            },
            {
                'text': 'How do you check if a key exists in a dictionary?',
                'difficulty': 'easy',
                'choices': [
                    ("'key' in dict", True),
                    ("dict['key']", False),
                    ("dict.has_key('key')", False),
                    ("dict.exists('key')", False),
                ]
            },
            {
                'text': 'What does dict.update() return?',
                'difficulty': 'medium',
                'choices': [
                    ('None (modifies dict in place)', True),
                    ('The updated dictionary', False),
                    ('The new key-value pairs', False),
                    ('True if successful', False),
                ]
            },
            # Set Operations
            {
                'text': 'What is the output of: {1, 2, 3} & {2, 3, 4}',
                'difficulty': 'medium',
                'choices': [
                    ('{2, 3}', True),
                    ('{1, 2, 3, 4}', False),
                    ('{1, 4}', False),
                    ('Error', False),
                ]
            },
            {
                'text': 'What is the output of: {1, 2, 3} | {2, 3, 4}',
                'difficulty': 'medium',
                'choices': [
                    ('{1, 2, 3, 4}', True),
                    ('{2, 3}', False),
                    ('{1, 4}', False),
                    ('Error', False),
                ]
            },
            {
                'text': 'Which method removes an element from a set?',
                'difficulty': 'easy',
                'choices': [
                    ('remove() or discard()', True),
                    ('pop()', False),
                    ('delete()', False),
                    ('clear()', False),
                ]
            },
            # Functions and Lambdas
            {
                'text': 'What is a lambda function?',
                'difficulty': 'medium',
                'choices': [
                    ('An anonymous function', True),
                    ('A built-in function', False),
                    ('A class method', False),
                    ('A generator function', False),
                ]
            },
            {
                'text': 'What is the output of: lambda x: x * 2)(5)',
                'difficulty': 'medium',
                'choices': [
                    ('10', True),
                    ('52', False),
                    ('Error', False),
                    ('25', False),
                ]
            },
            {
                'text': 'What does `*args` allow in a function?',
                'difficulty': 'medium',
                'choices': [
                    ('Variable number of positional arguments', True),
                    ('Variable number of keyword arguments', False),
                    ('Multiple return values', False),
                    ('Function overloading', False),
                ]
            },
            {
                'text': 'What does `**kwargs` allow in a function?',
                'difficulty': 'medium',
                'choices': [
                    ('Variable number of keyword arguments', True),
                    ('Variable number of positional arguments', False),
                    ('Multiple return values', False),
                    ('Function overloading', False),
                ]
            },
            # Exception Handling
            {
                'text': 'What does the `finally` block do in try-except?',
                'difficulty': 'medium',
                'choices': [
                    ('Always executes regardless of exceptions', True),
                    ('Only executes if no exception occurs', False),
                    ('Only executes if exception occurs', False),
                    ('Never executes', False),
                ]
            },
            {
                'text': 'What is raised when you access a non-existent dictionary key?',
                'difficulty': 'easy',
                'choices': [
                    ('KeyError', True),
                    ('IndexError', False),
                    ('ValueError', False),
                    ('AttributeError', False),
                ]
            },
            {
                'text': 'What exception is raised for division by zero?',
                'difficulty': 'easy',
                'choices': [
                    ('ZeroDivisionError', True),
                    ('ValueError', False),
                    ('ArithmeticError', False),
                    ('DivisionError', False),
                ]
            },
            # File Operations
            {
                'text': 'What mode opens a file for both reading and writing?',
                'difficulty': 'medium',
                'choices': [
                    ("'r+' or 'w+'", True),
                    ("'rw'", False),
                    ("'readwrite'", False),
                    ("'both'", False),
                ]
            },
            {
                'text': 'What is the correct way to open a file and ensure it closes?',
                'difficulty': 'medium',
                'choices': [
                    ('with open("file.txt") as f:', True),
                    ('open("file.txt").read()', False),
                    ('file("file.txt").read()', False),
                    ('read("file.txt")', False),
                ]
            },
            # OOP Concepts
            {
                'text': 'What is the first parameter of instance methods in a class?',
                'difficulty': 'easy',
                'choices': [
                    ('self', True),
                    ('this', False),
                    ('cls', False),
                    ('instance', False),
                ]
            },
            {
                'text': 'What is the first parameter of class methods?',
                'difficulty': 'medium',
                'choices': [
                    ('cls', True),
                    ('self', False),
                    ('class', False),
                    ('this', False),
                ]
            },
            {
                'text': 'What does `@staticmethod` decorator do?',
                'difficulty': 'medium',
                'choices': [
                    ('Creates a method that does not need self or cls', True),
                    ('Makes a method private', False),
                    ('Makes a method abstract', False),
                    ('Converts method to property', False),
                ]
            },
            {
                'text': 'What is inheritance in Python?',
                'difficulty': 'easy',
                'choices': [
                    ('A class can inherit from another class', True),
                    ('A function can inherit from another function', False),
                    ('A variable can inherit from another variable', False),
                    ('Only single inheritance is allowed', False),
                ]
            },
            {
                'text': 'What is method overriding?',
                'difficulty': 'medium',
                'choices': [
                    ('Defining a method in subclass that replaces parent method', True),
                    ('Calling a parent method from child', False),
                    ('Defining multiple methods with same name', False),
                    ('Preventing method access', False),
                ]
            },
            {
                'text': 'What does `super()` do?',
                'difficulty': 'medium',
                'choices': [
                    ('Calls parent class methods', True),
                    ('Calls child class methods', False),
                    ('Creates a superclass', False),
                    ('Removes inheritance', False),
                ]
            },
            # Decorators
            {
                'text': 'What is a decorator in Python?',
                'difficulty': 'hard',
                'choices': [
                    ('A function that modifies another function', True),
                    ('A class that modifies another class', False),
                    ('A built-in Python feature', False),
                    ('A syntax error', False),
                ]
            },
            {
                'text': 'What does `@property` decorator do?',
                'difficulty': 'medium',
                'choices': [
                    ('Makes a method accessible as an attribute', True),
                    ('Makes a variable accessible as a method', False),
                    ('Makes a method private', False),
                    ('Converts a class to a function', False),
                ]
            },
            # Generators and Iterators
            {
                'text': 'What keyword is used in a generator function?',
                'difficulty': 'medium',
                'choices': [
                    ('yield', True),
                    ('return', False),
                    ('generate', False),
                    ('produce', False),
                ]
            },
            {
                'text': 'What is the difference between a generator and a list?',
                'difficulty': 'hard',
                'choices': [
                    ('Generator is lazy, list is eager', True),
                    ('Generator is eager, list is lazy', False),
                    ('No difference', False),
                    ('Generator uses more memory', False),
                ]
            },
            {
                'text': 'What does `next()` do with an iterator?',
                'difficulty': 'medium',
                'choices': [
                    ('Returns the next item', True),
                    ('Returns all items', False),
                    ('Resets the iterator', False),
                    ('Raises StopIteration always', False),
                ]
            },
            # Comprehensions
            {
                'text': 'What is dictionary comprehension syntax?',
                'difficulty': 'medium',
                'choices': [
                    ('{key: value for item in iterable}', True),
                    ('[key: value for item in iterable]', False),
                    ('(key: value for item in iterable)', False),
                    ('dict(key: value for item in iterable)', False),
                ]
            },
            {
                'text': 'What is set comprehension syntax?',
                'difficulty': 'medium',
                'choices': [
                    ('{expression for item in iterable}', True),
                    ('[expression for item in iterable]', False),
                    ('(expression for item in iterable)', False),
                    ('set(expression for item in iterable)', False),
                ]
            },
            # Advanced Topics
            {
                'text': 'What is the Global Interpreter Lock (GIL)?',
                'difficulty': 'hard',
                'choices': [
                    ('A mutex that allows only one thread at a time', True),
                    ('A global variable lock', False),
                    ('A file locking mechanism', False),
                    ('A database lock', False),
                ]
            },
            {
                'text': 'What does `__name__ == "__main__"` check?',
                'difficulty': 'medium',
                'choices': [
                    ('If script is run directly (not imported)', True),
                    ('If script is imported', False),
                    ('If script has a main function', False),
                    ('If script is in main directory', False),
                ]
            },
            {
                'text': 'What is a context manager?',
                'difficulty': 'hard',
                'choices': [
                    ('An object with __enter__ and __exit__ methods', True),
                    ('A function that manages contexts', False),
                    ('A class that manages variables', False),
                    ('A built-in Python type', False),
                ]
            },
            {
                'text': 'What does `__str__` method do?',
                'difficulty': 'medium',
                'choices': [
                    ('Returns string representation of object', True),
                    ('Converts object to string type', False),
                    ('Prints object to console', False),
                    ('Compares object to string', False),
                ]
            },
            {
                'text': 'What does `__repr__` method do?',
                'difficulty': 'hard',
                'choices': [
                    ('Returns official string representation', True),
                    ('Returns informal string representation', False),
                    ('Reverses the object', False),
                    ('Creates a copy', False),
                ]
            },
        ]

        # Coding Questions
        coding_questions = [
            {
                'text': 'Write a function `add_numbers(a, b)` that returns the sum of two numbers.',
                'difficulty': 'easy',
                'starter_code': 'def add_numbers(a, b):\n    # Your code here\n    pass',
                'solution': 'def add_numbers(a, b):\n    return a + b',
                'test_cases': [
                    ({'a': 5, 'b': 3}, 8),
                    ({'a': -1, 'b': 1}, 0),
                    ({'a': 10, 'b': 20}, 30),
                ]
            },
            {
                'text': 'Write a function `is_even(n)` that returns True if n is even, False otherwise.',
                'difficulty': 'easy',
                'starter_code': 'def is_even(n):\n    # Your code here\n    pass',
                'solution': 'def is_even(n):\n    return n % 2 == 0',
                'test_cases': [
                    ({'n': 4}, True),
                    ({'n': 5}, False),
                    ({'n': 0}, True),
                    ({'n': -2}, True),
                ]
            },
            {
                'text': 'Write a function `reverse_string(s)` that returns the reversed version of string s.',
                'difficulty': 'easy',
                'starter_code': 'def reverse_string(s):\n    # Your code here\n    pass',
                'solution': 'def reverse_string(s):\n    return s[::-1]',
                'test_cases': [
                    ({'s': "hello"}, "olleh"),
                    ({'s': "Python"}, "nohtyP"),
                    ({'s': ""}, ""),
                    ({'s': "a"}, "a"),
                ]
            },
            {
                'text': 'Write a function `find_max(numbers)` that returns the maximum number from a list.',
                'difficulty': 'easy',
                'starter_code': 'def find_max(numbers):\n    # Your code here\n    pass',
                'solution': 'def find_max(numbers):\n    if not numbers:\n        return None\n    return max(numbers)',
                'test_cases': [
                    ({'numbers': [1, 5, 3, 9, 2]}, 9),
                    ({'numbers': [-5, -2, -10]}, -2),
                    ({'numbers': [42]}, 42),
                ]
            },
            {
                'text': 'Write a function `count_vowels(s)` that returns the number of vowels (a, e, i, o, u) in a string.',
                'difficulty': 'medium',
                'starter_code': 'def count_vowels(s):\n    # Your code here\n    pass',
                'solution': 'def count_vowels(s):\n    vowels = "aeiouAEIOU"\n    return sum(1 for char in s if char in vowels)',
                'test_cases': [
                    ({'s': "hello"}, 2),
                    ({'s': "Python"}, 1),
                    ({'s': "aeiou"}, 5),
                    ({'s': "bcdfg"}, 0),
                ]
            },
            {
                'text': 'Write a function `factorial(n)` that returns the factorial of n. (factorial(5) = 5*4*3*2*1 = 120)',
                'difficulty': 'medium',
                'starter_code': 'def factorial(n):\n    # Your code here\n    pass',
                'solution': 'def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)',
                'test_cases': [
                    ({'n': 5}, 120),
                    ({'n': 3}, 6),
                    ({'n': 0}, 1),
                    ({'n': 1}, 1),
                ]
            },
            {
                'text': 'Write a function `fibonacci(n)` that returns the nth Fibonacci number. (fibonacci(0)=0, fibonacci(1)=1)',
                'difficulty': 'medium',
                'starter_code': 'def fibonacci(n):\n    # Your code here\n    pass',
                'solution': 'def fibonacci(n):\n    if n <= 1:\n        return n\n    a, b = 0, 1\n    for _ in range(2, n + 1):\n        a, b = b, a + b\n    return b',
                'test_cases': [
                    ({'n': 0}, 0),
                    ({'n': 1}, 1),
                    ({'n': 5}, 5),
                    ({'n': 7}, 13),
                ]
            },
            {
                'text': 'Write a function `is_palindrome(s)` that returns True if s is a palindrome (reads same forwards and backwards), False otherwise.',
                'difficulty': 'medium',
                'starter_code': 'def is_palindrome(s):\n    # Your code here\n    pass',
                'solution': 'def is_palindrome(s):\n    s = s.lower().replace(" ", "")\n    return s == s[::-1]',
                'test_cases': [
                    ({'s': "racecar"}, True),
                    ({'s': "hello"}, False),
                    ({'s': "A man a plan a canal Panama"}, True),
                    ({'s': "level"}, True),
                ]
            },
            {
                'text': 'Write a function `remove_duplicates(lst)` that returns a list with duplicates removed while preserving order.',
                'difficulty': 'medium',
                'starter_code': 'def remove_duplicates(lst):\n    # Your code here\n    pass',
                'solution': 'def remove_duplicates(lst):\n    seen = set()\n    result = []\n    for item in lst:\n        if item not in seen:\n            seen.add(item)\n            result.append(item)\n    return result',
                'test_cases': [
                    ({'lst': [1, 2, 2, 3, 3, 3, 4]}, [1, 2, 3, 4]),
                    ({'lst': ["a", "b", "a", "c"]}, ["a", "b", "c"]),
                    ({'lst': [1, 1, 1]}, [1]),
                ]
            },
            {
                'text': 'Write a function `two_sum(nums, target)` that returns indices of two numbers that add up to target. Return as list [index1, index2].',
                'difficulty': 'hard',
                'starter_code': 'def two_sum(nums, target):\n    # Your code here\n    pass',
                'solution': 'def two_sum(nums, target):\n    num_map = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in num_map:\n            return [num_map[complement], i]\n        num_map[num] = i\n    return []',
                'test_cases': [
                    ({'nums': [2, 7, 11, 15], 'target': 9}, [0, 1]),
                    ({'nums': [3, 2, 4], 'target': 6}, [1, 2]),
                    ({'nums': [3, 3], 'target': 6}, [0, 1]),
                ]
            },
            {
                'text': 'Write a function `merge_sorted_lists(list1, list2)` that merges two sorted lists into one sorted list.',
                'difficulty': 'hard',
                'starter_code': 'def merge_sorted_lists(list1, list2):\n    # Your code here\n    pass',
                'solution': 'def merge_sorted_lists(list1, list2):\n    result = []\n    i, j = 0, 0\n    while i < len(list1) and j < len(list2):\n        if list1[i] <= list2[j]:\n            result.append(list1[i])\n            i += 1\n        else:\n            result.append(list2[j])\n            j += 1\n    result.extend(list1[i:])\n    result.extend(list2[j:])\n    return result',
                'test_cases': [
                    ({'list1': [1, 3, 5], 'list2': [2, 4, 6]}, [1, 2, 3, 4, 5, 6]),
                    ({'list1': [1, 2, 3], 'list2': [4, 5, 6]}, [1, 2, 3, 4, 5, 6]),
                    ({'list1': [], 'list2': [1, 2]}, [1, 2]),
                ]
            },
            {
                'text': 'Write a function `fizzbuzz(n)` that returns a list of numbers from 1 to n, but replaces multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".',
                'difficulty': 'medium',
                'starter_code': 'def fizzbuzz(n):\n    # Your code here\n    pass',
                'solution': 'def fizzbuzz(n):\n    result = []\n    for i in range(1, n + 1):\n        if i % 15 == 0:\n            result.append("FizzBuzz")\n        elif i % 3 == 0:\n            result.append("Fizz")\n        elif i % 5 == 0:\n            result.append("Buzz")\n        else:\n            result.append(i)\n    return result',
                'test_cases': [
                    ({'n': 15}, [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]),
                ]
            },
            # Additional Easy Coding Questions
            {
                'text': 'Write a function `multiply(a, b)` that returns the product of two numbers.',
                'difficulty': 'easy',
                'starter_code': 'def multiply(a, b):\n    # Your code here\n    pass',
                'solution': 'def multiply(a, b):\n    return a * b',
                'test_cases': [
                    ({'a': 5, 'b': 4}, 20),
                    ({'a': -2, 'b': 3}, -6),
                    ({'a': 0, 'b': 100}, 0),
                ]
            },
            {
                'text': 'Write a function `square(n)` that returns the square of a number.',
                'difficulty': 'easy',
                'starter_code': 'def square(n):\n    # Your code here\n    pass',
                'solution': 'def square(n):\n    return n ** 2',
                'test_cases': [
                    ({'n': 5}, 25),
                    ({'n': -3}, 9),
                    ({'n': 0}, 0),
                ]
            },
            {
                'text': 'Write a function `capitalize_words(s)` that capitalizes the first letter of each word in a string.',
                'difficulty': 'easy',
                'starter_code': 'def capitalize_words(s):\n    # Your code here\n    pass',
                'solution': 'def capitalize_words(s):\n    return s.title()',
                'test_cases': [
                    ({'s': "hello world"}, "Hello World"),
                    ({'s': "python programming"}, "Python Programming"),
                    ({'s': "a"}, "A"),
                ]
            },
            {
                'text': 'Write a function `find_min(numbers)` that returns the minimum number from a list.',
                'difficulty': 'easy',
                'starter_code': 'def find_min(numbers):\n    # Your code here\n    pass',
                'solution': 'def find_min(numbers):\n    if not numbers:\n        return None\n    return min(numbers)',
                'test_cases': [
                    ({'numbers': [5, 2, 9, 1]}, 1),
                    ({'numbers': [-5, -2, -10]}, -10),
                    ({'numbers': [42]}, 42),
                ]
            },
            {
                'text': 'Write a function `sum_list(numbers)` that returns the sum of all numbers in a list.',
                'difficulty': 'easy',
                'starter_code': 'def sum_list(numbers):\n    # Your code here\n    pass',
                'solution': 'def sum_list(numbers):\n    return sum(numbers)',
                'test_cases': [
                    ({'numbers': [1, 2, 3, 4]}, 10),
                    ({'numbers': [-1, 0, 1]}, 0),
                    ({'numbers': []}, 0),
                ]
            },
            {
                'text': 'Write a function `count_words(s)` that returns the number of words in a string.',
                'difficulty': 'easy',
                'starter_code': 'def count_words(s):\n    # Your code here\n    pass',
                'solution': 'def count_words(s):\n    return len(s.split())',
                'test_cases': [
                    ({'s': "hello world"}, 2),
                    ({'s': "Python is great"}, 3),
                    ({'s': ""}, 0),
                ]
            },
            # Additional Medium Coding Questions
            {
                'text': 'Write a function `find_longest_word(words)` that returns the longest word from a list of words.',
                'difficulty': 'medium',
                'starter_code': 'def find_longest_word(words):\n    # Your code here\n    pass',
                'solution': 'def find_longest_word(words):\n    if not words:\n        return None\n    return max(words, key=len)',
                'test_cases': [
                    ({'words': ["cat", "dog", "elephant"]}, "elephant"),
                    ({'words': ["a", "ab", "abc"]}, "abc"),
                    ({'words': ["hello"]}, "hello"),
                ]
            },
            {
                'text': 'Write a function `find_common_elements(list1, list2)` that returns a list of common elements between two lists.',
                'difficulty': 'medium',
                'starter_code': 'def find_common_elements(list1, list2):\n    # Your code here\n    pass',
                'solution': 'def find_common_elements(list1, list2):\n    return [x for x in list1 if x in list2]',
                'test_cases': [
                    ({'list1': [1, 2, 3], 'list2': [2, 3, 4]}, [2, 3]),
                    ({'list1': [1, 2, 3], 'list2': [4, 5, 6]}, []),
                    ({'list1': ["a", "b"], 'list2': ["b", "c"]}, ["b"]),
                ]
            },
            {
                'text': 'Write a function `is_prime(n)` that returns True if n is a prime number, False otherwise.',
                'difficulty': 'medium',
                'starter_code': 'def is_prime(n):\n    # Your code here\n    pass',
                'solution': 'def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n ** 0.5) + 1):\n        if n % i == 0:\n            return False\n    return True',
                'test_cases': [
                    ({'n': 7}, True),
                    ({'n': 4}, False),
                    ({'n': 2}, True),
                    ({'n': 1}, False),
                ]
            },
            {
                'text': 'Write a function `power(base, exponent)` that returns base raised to the power of exponent.',
                'difficulty': 'medium',
                'starter_code': 'def power(base, exponent):\n    # Your code here\n    pass',
                'solution': 'def power(base, exponent):\n    return base ** exponent',
                'test_cases': [
                    ({'base': 2, 'exponent': 3}, 8),
                    ({'base': 5, 'exponent': 2}, 25),
                    ({'base': 10, 'exponent': 0}, 1),
                ]
            },
            {
                'text': 'Write a function `reverse_list(lst)` that returns a reversed list.',
                'difficulty': 'medium',
                'starter_code': 'def reverse_list(lst):\n    # Your code here\n    pass',
                'solution': 'def reverse_list(lst):\n    return lst[::-1]',
                'test_cases': [
                    ({'lst': [1, 2, 3, 4]}, [4, 3, 2, 1]),
                    ({'lst': ["a", "b", "c"]}, ["c", "b", "a"]),
                    ({'lst': []}, []),
                ]
            },
            {
                'text': 'Write a function `count_characters(s)` that returns a dictionary with character counts.',
                'difficulty': 'medium',
                'starter_code': 'def count_characters(s):\n    # Your code here\n    pass',
                'solution': 'def count_characters(s):\n    result = {}\n    for char in s:\n        result[char] = result.get(char, 0) + 1\n    return result',
                'test_cases': [
                    ({'s': "hello"}, {'h': 1, 'e': 1, 'l': 2, 'o': 1}),
                    ({'s': "aabbcc"}, {'a': 2, 'b': 2, 'c': 2}),
                    ({'s': ""}, {}),
                ]
            },
            {
                'text': 'Write a function `sum_of_squares(n)` that returns the sum of squares from 1 to n.',
                'difficulty': 'medium',
                'starter_code': 'def sum_of_squares(n):\n    # Your code here\n    pass',
                'solution': 'def sum_of_squares(n):\n    return sum(i**2 for i in range(1, n + 1))',
                'test_cases': [
                    ({'n': 3}, 14),  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
                    ({'n': 5}, 55),  # 1+4+9+16+25 = 55
                    ({'n': 1}, 1),
                ]
            },
            {
                'text': 'Write a function `find_missing_number(numbers)` that finds the missing number in a sequence from 1 to n where one number is missing.',
                'difficulty': 'medium',
                'starter_code': 'def find_missing_number(numbers):\n    # Your code here\n    pass',
                'solution': 'def find_missing_number(numbers):\n    n = len(numbers) + 1\n    expected_sum = n * (n + 1) // 2\n    actual_sum = sum(numbers)\n    return expected_sum - actual_sum',
                'test_cases': [
                    ({'numbers': [1, 2, 4, 5]}, 3),
                    ({'numbers': [1, 3, 4, 5]}, 2),
                    ({'numbers': [2, 3, 4, 5]}, 1),
                ]
            },
            {
                'text': 'Write a function `rotate_list(lst, k)` that rotates a list to the right by k positions.',
                'difficulty': 'medium',
                'starter_code': 'def rotate_list(lst, k):\n    # Your code here\n    pass',
                'solution': 'def rotate_list(lst, k):\n    if not lst:\n        return []\n    k = k % len(lst)\n    return lst[-k:] + lst[:-k]',
                'test_cases': [
                    ({'lst': [1, 2, 3, 4, 5], 'k': 2}, [4, 5, 1, 2, 3]),
                    ({'lst': [1, 2, 3], 'k': 1}, [3, 1, 2]),
                    ({'lst': [1, 2, 3], 'k': 3}, [1, 2, 3]),
                ]
            },
            # Additional Hard Coding Questions
            {
                'text': 'Write a function `binary_search(arr, target)` that implements binary search and returns the index of target, or -1 if not found.',
                'difficulty': 'hard',
                'starter_code': 'def binary_search(arr, target):\n    # Your code here\n    pass',
                'solution': 'def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1',
                'test_cases': [
                    ({'arr': [1, 3, 5, 7, 9], 'target': 5}, 2),
                    ({'arr': [1, 3, 5, 7, 9], 'target': 3}, 1),
                    ({'arr': [1, 3, 5, 7, 9], 'target': 10}, -1),
                ]
            },
            {
                'text': 'Write a function `is_anagram(s1, s2)` that returns True if s1 and s2 are anagrams (same characters, different order).',
                'difficulty': 'hard',
                'starter_code': 'def is_anagram(s1, s2):\n    # Your code here\n    pass',
                'solution': 'def is_anagram(s1, s2):\n    return sorted(s1.lower()) == sorted(s2.lower())',
                'test_cases': [
                    ({'s1': "listen", 's2': "silent"}, True),
                    ({'s1': "hello", 's2': "world"}, False),
                    ({'s1': "rail safety", 's2': "fairy tales"}, True),
                ]
            },
            {
                'text': 'Write a function `find_max_subarray_sum(arr)` that finds the maximum sum of a contiguous subarray.',
                'difficulty': 'hard',
                'starter_code': 'def find_max_subarray_sum(arr):\n    # Your code here\n    pass',
                'solution': 'def find_max_subarray_sum(arr):\n    if not arr:\n        return 0\n    max_sum = current_sum = arr[0]\n    for num in arr[1:]:\n        current_sum = max(num, current_sum + num)\n        max_sum = max(max_sum, current_sum)\n    return max_sum',
                'test_cases': [
                    ({'arr': [-2, 1, -3, 4, -1, 2, 1, -5, 4]}, 6),  # [4, -1, 2, 1]
                    ({'arr': [1, 2, 3, 4]}, 10),
                    ({'arr': [-1, -2, -3]}, -1),
                ]
            },
            {
                'text': 'Write a function `group_anagrams(words)` that groups words that are anagrams together. Return a list of lists.',
                'difficulty': 'hard',
                'starter_code': 'def group_anagrams(words):\n    # Your code here\n    pass',
                'solution': 'def group_anagrams(words):\n    groups = {}\n    for word in words:\n        key = "".join(sorted(word.lower()))\n        if key not in groups:\n            groups[key] = []\n        groups[key].append(word)\n    return list(groups.values())',
                'test_cases': [
                    ({'words': ["eat", "tea", "tan", "ate", "nat", "bat"]}, [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
                ],
                'custom_validation': True  # Order doesn't matter
            },
            {
                'text': 'Write a function `longest_common_prefix(strings)` that finds the longest common prefix among an array of strings.',
                'difficulty': 'hard',
                'starter_code': 'def longest_common_prefix(strings):\n    # Your code here\n    pass',
                'solution': 'def longest_common_prefix(strings):\n    if not strings:\n        return ""\n    prefix = strings[0]\n    for string in strings[1:]:\n        while not string.startswith(prefix):\n            prefix = prefix[:-1]\n            if not prefix:\n                return ""\n    return prefix',
                'test_cases': [
                    ({'strings': ["flower", "flow", "flight"]}, "fl"),
                    ({'strings': ["dog", "racecar", "car"]}, ""),
                    ({'strings': ["interspecies", "interstellar", "interstate"]}, "inters"),
                ]
            },
        ]

        # Add multiple choice questions
        self.stdout.write('Adding multiple choice questions...')
        for q_data in mc_questions:
            question, created = Question.objects.get_or_create(
                category=category,
                text=q_data['text'],
                defaults={
                    'question_type': 'multiple_choice',
                    'difficulty': q_data['difficulty']
                }
            )
            
            if created:
                for choice_text, is_correct in q_data['choices']:
                    Choice.objects.create(
                        question=question,
                        text=choice_text,
                        is_correct=is_correct
                    )
                self.stdout.write(self.style.SUCCESS(f'Created: {q_data["text"][:50]}...'))

        # Add coding questions
        self.stdout.write('Adding coding questions...')
        for q_data in coding_questions:
            question, created = Question.objects.get_or_create(
                category=category,
                text=q_data['text'],
                defaults={
                    'question_type': 'coding',
                    'difficulty': q_data['difficulty'],
                    'starter_code': q_data.get('starter_code', ''),
                    'solution': q_data.get('solution', '')
                }
            )
            
            if created:
                for input_data, expected_output in q_data.get('test_cases', []):
                    TestCase.objects.create(
                        question=question,
                        input_data=json.dumps(input_data),
                        expected_output=json.dumps(expected_output),
                        is_hidden=False
                    )
                self.stdout.write(self.style.SUCCESS(f'Created: {q_data["text"][:50]}...'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully populated {len(mc_questions)} multiple choice and {len(coding_questions)} coding questions!'))

