from django.contrib import admin
from django.urls import path
from .views import QuizList

app_name="quiz"

urlpatterns = [
    # path('api/', include('api.urls', namespace='api')),
    path('quizes/', QuizList.as_view(), name='list'),
]