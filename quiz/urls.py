from django.contrib import admin
from django.urls import path
from .views import QuizList, QuizDetail

app_name="quiz"

urlpatterns = [
    path('<int:pk>', QuizDetail.as_view(), name='retrieve'),
    path('', QuizList.as_view(), name='list'),
]