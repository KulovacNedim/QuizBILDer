from rest_framework import serializers
from quiz.models import Quiz
from question.models import Question
from question.models import Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Answer
        fields = [
            'id',
            'answer',
            'is_correct',
        ]

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:

        model = Question
        fields = [
            'id',
            'title',
            'points',
            'difficulty',
            'is_active',
            'question_type',
            'is_for_exam',
            'created_at',
            'updated_at',
            'answers'
        ]





class QuizSerializer(serializers.ModelSerializer):

    # answer = AnswerSerializer(many=True, read_only=True)
    # question = "NEDIM"
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:

        model = Quiz
        fields = [
            'id',
            'name',
            'subcategory',
            'created_by',
            'is_active',
            'expires_at',
            'created_at',
            'updated_at',
            'questions',
            # 'points',
            # 'answer'
        ]