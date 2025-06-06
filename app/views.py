from rest_framework.response import Response
from rest_framework import status
from .models import Student, School
from .serializers import StudentSerializer, SchoolSerializer
from rest_framework.decorators import api_view


@api_view(["GET"])
def list_schools(request):
    schools = School.objects.all()
    serializer = SchoolSerializer(schools, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_school(request):
    serializer = SchoolSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "School has been created",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def school_details(request, id):
    # school = School.objects.get(id=id)
    try:
        school = School.objects.get(id=id)
    except School.DoesNotExist:
        return Response({"message": "The school you are trying to access is not there"})

    if request.method == "GET":
        try:
            school = School.objects.get(id=id)
        except School.DoesNotExist:
            return None
        serializer = SchoolSerializer(school)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = SchoolSerializer(instance=school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "School has been edited",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        school.delete()
        return Response({
                "message": "School has been deleted"
            }, status=status.HTTP_204_NO_CONTENT)
    

@api_view(["GET", "POST"])
def students_list_create(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Student created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

@api_view(["PUT", "GET", "DELETE"])
def student_details(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"data": "That student doesnot exist"})
    
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = StudentSerializer(instance=student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Student details have been updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        student.delete()
        return Response({
                "message": "Student details have been updated successfully"
        }, status=status.HTTP_204_NO_CONTENT)


