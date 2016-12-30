from django.contrib.auth import get_user_model

from rest_framework.serializers import (
    CharField, ModelSerializer, ValidationError)

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    password2 = CharField(label="Password confirmation",
                    write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2',
        ]

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):

        username = validated_data.get('username', None)
        password = validated_data.get('password', None)
        user_obj = User(username = username)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

    def validate_username(self, value):
        data = self.get_initial()
        username = data.get('username', None)
        user_qs = User.objects.filter(username=username)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return value

    def validate_password(self, value):
        data = self.get_initial()
        password = data.get('password', None)
        password2 = data.get('password2', None)
        if password != password2:
            raise ValidationError("Password doesn't match.")
        return value


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
        ]
