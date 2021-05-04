from rest_framework import generics
from quiz.models import Quiz
from .serializers import QuizSerializer

class QuizList(generics.ListAPIView):
  queryset = Quiz.objects.all()
  serializer_class = QuizSerializer
  pass

class QuizDetail(generics.RetrieveDestroyAPIView):
  queryset = Quiz.objects.all()
  pass