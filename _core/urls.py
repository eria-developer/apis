from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/fbv/", include("app.urls")),
    path("api/second-way/", include("app.urls_second_way"))
]
