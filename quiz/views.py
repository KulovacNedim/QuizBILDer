from rest_framework import generics
from quiz.models import Quiz
from .serializers import QuizSerializer

class QuizList(generics.ListAPIView):
  queryset = Quiz.objects.all()
  serializer_class = QuizSerializer

class QuizDetail(generics.RetrieveAPIView):
  queryset = Quiz.objects.all()
  serializer_class = QuizSerializer