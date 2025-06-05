from rest_framework import serializers
from .models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ["id", "name", "address"]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "age", "school"]