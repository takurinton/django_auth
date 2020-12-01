from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class IndexView(APIView):
    def get(self, request):
        me = {
            'name': 'takurinton', 
            'age': 21, 
            'hoge': 'fuga', 
        }
        return Response(me)
