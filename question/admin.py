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
    'is_for_exam'
  ]
  list_display = [
    'title',
    'updated_at'
  ]
  inlines = [
    AnswerInlineModel,
  ]

# @admin.register(models.Answer)

class AnswerAdmin(admin.ModelAdmin):
  list_display = [
    'answer',
    'is_correct',
    'question'
  ]

