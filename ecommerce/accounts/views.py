from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username,password)
        # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user = User(username=username,is_staff = True)
        user.set_password(password)
        refresh = RefreshToken.for_user(user)
        user.save()
        return Response({
            "status":'success',
            "user_id":user.id,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })
