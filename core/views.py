from .models import Contact
from rest_framework import viewsets
from .serializers import ContactSerialize, UserSerialize
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.permissions import AllowAny


# Create your views here.


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerialize


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerialize
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.method == "GET":
            return None
        users = User.objects.filter(is_superuser=False)
        return users

    def create(self, request, *args, **kwargs):
        data = request.data
        if not data["username"] or not data["password"] or not data["email"]:
            return JsonResponse({"message": "Invalid Credentials"}, status=400)
        users = User.objects.all()
        for e in users:
            if data["email"] == e.email or data["username"] == e.username:
                return JsonResponse({"error": "existing email or username"}, status=422)
        user = User.objects.create_user(
            username=data["username"], password=data["password"], email=data["email"],
        )
        serializer = UserSerialize(user)
        return Response(serializer.data)
