from rest_framework import serializers
from quiz.models import Quiz, SubCategory
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


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = SubCategory
        fields = [
            'id',
            'category',
            'name',
            'is_active',
            'created_at',
            'updated_at',
        ]


class QuizSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True, read_only=True)
    subcategory = SubCategorySerializer(read_only=True)

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
        ]