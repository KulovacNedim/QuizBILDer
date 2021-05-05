from django.contrib import admin
from question.models import Question, Answer
from nested_admin import NestedModelAdmin, NestedTabularInline

from . import models


class SubcategoryInlineModel(admin.TabularInline):
  model = models.SubCategory
  fields = [
    'name',
    'is_active',
  ]

@admin.register(models.Category)

class CategoryAdmin(admin.ModelAdmin):
  fields = [
    'name',
    'is_active',
  ]
  list_display = [
    'name',
    'is_active',
  ]
  inlines = [
    SubcategoryInlineModel,
  ]

class QuestionInline(admin.TabularInline):
    model = Question.quiz.through

@admin.register(models.Quiz)

class QuizAdmin(admin.ModelAdmin):
  fields = [
    'name',
    'subcategory',
    'created_by',
    'is_active',
    'expires_at',
  ]
  list_display = [
    'name',
    'subcategory',
    'is_active',
  ]
  inlines = [
    QuestionInline,
  ]
  