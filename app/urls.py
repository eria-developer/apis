from django.urls import path
from .views import list_schools, add_school, school_details

urlpatterns = [
    path("list-schools/", list_schools),
    path("add-schools/", add_school),
    path("schools/<int:id>/", school_details),
]
