from django.urls import path
from .views_second_way import SchoolView, SchoolDetailsView

urlpatterns = [
    path("school/", SchoolView.as_view()),
    path("school/<int:id>/", SchoolDetailsView.as_view())
]

