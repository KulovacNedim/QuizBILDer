from django.contrib import admin
from django.urls import path
from .views import QuizList

app_name="quiz"

urlpatterns = [
    path('quizes/', QuizList.as_view(), name='list'),
]