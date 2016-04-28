from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )


User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }