from django.contrib import admin
from .models import Category, Question, Choice, TestCase

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'question_type', 'difficulty', 'category', 'created_at']
    list_filter = ['question_type', 'difficulty', 'category']
    search_fields = ['text']
    filter_horizontal = []

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['text', 'question', 'is_correct']
    list_filter = ['is_correct', 'question']
    search_fields = ['text', 'question__text']

@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['question', 'input_data', 'expected_output', 'is_hidden']
    list_filter = ['is_hidden', 'question']
    search_fields = ['question__text']
