from django.urls import path
from .views import list_schools, add_school, school_details, students_list_create, student_details

urlpatterns = [
    # school urls 
    path("list-schools/", list_schools),
    path("add-schools/", add_school),
    path("schools/<int:id>/", school_details),

    # student urls 
    path("students/", students_list_create),
    path("students/<int:id>/", student_details),
]
