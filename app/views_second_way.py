from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student, School
from .serializers import StudentSerializer, SchoolSerializer


class SchoolView(APIView):
    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "School has been saved",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

    
    

class SchoolDetailsView(APIView):
    def get_school(self, id):
        try:
            school = School.objects.get(id=id)
        except School.DoesNotExist:
            return None
        
        return school
        
    def put(self, request, id):
        school = self.get_school(id)

        serializer = SchoolSerializer(instance=school, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "School has been updated",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

    def delete(self, request, id):
        school = self.get_school(id)
        if school is not None:
            school.delete()
            return Response({"data": "School has been removed"})
        return Response({"data": "That school teliiyo man"})
    

        