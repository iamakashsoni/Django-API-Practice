from rest_framework import serializers
from .models import *

class DoctorSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="Enter Doctor Id")
    name = serializers.CharField(label="Enter Doctor Name")
    specialist = serializers.CharField(label="Enter Doctor Specialization")

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"