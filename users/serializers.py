from rest_framework import serializers
from users.models import User
from django.shortcuts import get_object_or_404

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        email = attrs.get('email')
        user_name = attrs.get('user_name', '')
        user = User.objects.filter(email=email)

        if len(user) > 0:
            raise serializers.ValidationError(f'User with email {email} already exists')

        if not user_name.isalnum():
            raise serializers.ValidationError('The username has to contain anly alphanumeric characters')

        return attrs


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'user_name',
            'first_name',
            'last_name',
        ]