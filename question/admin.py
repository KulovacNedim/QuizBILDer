from django.contrib import admin

from . import models

class AnswerInlineModel(admin.TabularInline):
  model = models.Answer
  fields = [
    'answer',
    'is_correct',
    'is_active',
  ]

@admin.register(models.Question)

class QuestionAdmin(admin.ModelAdmin):
  fields = [
    'quiz',
    'title',
    'points',
    'difficulty',
    'is_active',
    'question_type',
    'subcategories',
    'is_for_exam'
  ]
  list_display = [
    'title',
    'updated_at'
  ]
  inlines = [
    AnswerInlineModel,
  ]

