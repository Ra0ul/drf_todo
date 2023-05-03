from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "name",
            "gender",
            "age",
            "intro",
            "password"
        )

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        print(password)
        user.set_password(password)
        user.save()
        return user

    def update(self, user, validated_data):
        user = super().update(validated_data)
        password = user.password

        user.set_password(password)
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['name'] = user.name
        token['gender'] = user.gender
        token['age'] = user.age
        token['intro'] = user.intro

        return token
