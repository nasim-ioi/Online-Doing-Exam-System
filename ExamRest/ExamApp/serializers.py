from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, SerializerMethodField
from .models import *

class QuestionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Questions
        fields = ('id', 'question', 'url')

class QuestionDetailSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields = ('options',)

class SingUpSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("Username"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

class AnsewrSerializer(serializers.Serializer):
    ansewr = serializers.JSONField()


