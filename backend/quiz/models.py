from django.db import models
import json

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('multiple_choice', 'Multiple Choice'),
        ('coding', 'Coding Question'),
    ]
    
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    category = models.ForeignKey(Category, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES, default='multiple_choice')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    created_at = models.DateTimeField(auto_now_add=True)
    
    # For coding questions
    starter_code = models.TextField(blank=True, help_text="Initial code template for coding questions")
    solution = models.TextField(blank=True, help_text="Expected solution code")
    
    def __str__(self):
        return self.text[:50]
    
    class Meta:
        ordering = ['-created_at']

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text

class TestCase(models.Model):
    """Test cases for coding questions"""
    question = models.ForeignKey(Question, related_name='test_cases', on_delete=models.CASCADE)
    input_data = models.TextField(help_text="Input as JSON string")
    expected_output = models.TextField(help_text="Expected output as JSON string")
    is_hidden = models.BooleanField(default=False, help_text="Hide test case from user")
    
    def __str__(self):
        return f"Test case for {self.question.text[:30]}"
    
    def get_input(self):
        """Parse input JSON"""
        try:
            return json.loads(self.input_data)
        except:
            return self.input_data
    
    def get_expected_output(self):
        """Parse expected output JSON"""
        try:
            return json.loads(self.expected_output)
        except:
            return self.expected_output
