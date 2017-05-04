from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model, authenticate
from django.db.models import Q

from rest_framework.serializers import (
    EmailField,
    CharField,

    ModelSerializer
)

from rest_framework.validators import (
    ValidationError
)

User = get_user_model()


class CreateUserSerializer(ModelSerializer):
    username = CharField(label='Username', trim_whitespace=True)
    email = EmailField(label='Email Address', trim_whitespace=True)
    password = CharField(label='Password', style={'input_type': 'password'}, trim_whitespace=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate_email(self, value):
        user_qs = User.objects.filter(email=value)
        if user_qs.exists():
            raise ValidationError('A user with this email address already exist')
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class LoginUserSerializer(ModelSerializer):
    token = CharField(label='Token', required=False, allow_blank=True, allow_null=True,  read_only=True)
    username = CharField(label='Username', required=False, trim_whitespace=True)
    email = EmailField(label='Email Address', required=False, trim_whitespace=True)
    password = CharField(label='Password', required=True, style={'input_type': 'password'}, trim_whitespace=True)

    class Meta:
        model = User
        fields = [
            'token',
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        user_obj = None
        email = data.get('email', None)
        username = data.get('username', None)
        password = data['password']
        if email is None and username is None:
            raise ValidationError("A username or email is required to login.")
        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct().exclude(email__isnull=True)
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This email/username is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials. Please try again.")
        else:
            data['token'] = 'SOME RANDOM TOKEN'
        return data

