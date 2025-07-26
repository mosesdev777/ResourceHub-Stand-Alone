from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("resourcehub/", include("resourcehub.urls", namespace="resourcehub")),
]
