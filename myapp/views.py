from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User

class IndexView(APIView):
    def get(self, request):
        user = request.user
        res = {
            'username': user.username, 
            'is_staff': user.is_staff, 
            'is_active': user.is_active, 
            'created_at': user.created_at, 
        }
        
        return Response(res)
