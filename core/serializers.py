from .models import Contact
from rest_framework import serializers
from django.contrib.auth.models import User


class ContactSerialize(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["email", "name", "message", "status"]


class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email","username"]
