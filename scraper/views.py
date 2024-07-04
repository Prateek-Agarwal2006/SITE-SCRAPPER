from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .scrapper import get_data
from .serializers import GPUDataSerializer
from django.http import JsonResponse

# Create your views here.



class GPUDataView(APIView):
    def get(self, request):
        data = get_data()
        serializer = GPUDataSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    


def index(request):
    return render(request, 'index.html')    
