from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated

class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        print(request.user)
        return Response({'success':'you are authenticated'})


# Create your views here.
class ProductView(APIView):

    def get(self, request):
        queryset = Product.objects.all()
        serializers = ProductSerializer(queryset, many=True)
        return Response(serializers.data)

