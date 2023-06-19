from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.

class DoctorApiView(APIView):
    serializer_class = DoctorSerializer
    def get(self, request):
        allDoctor = Doctor.objects.all().values()
        return Response({"Message":"List of Doctors", "Doctor List":allDoctor})
    
    def post(self, request):
        print('Request data is:', request.data)
        serializer_obj = DoctorSerializer(data=request.data)
        if(serializer_obj.is_valid()):
            Doctor.objects.create(id=serializer_obj.data.get("id"),
                                name = serializer_obj.data.get("name"),
                                specialist = serializer_obj.data.get("specialist"))
        
        doctor = Doctor.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New doctor added.", "Doctor":doctor})
    
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientSerializer