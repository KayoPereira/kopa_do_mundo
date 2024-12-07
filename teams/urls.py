# type: ignore
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet

router = DefaultRouter()
router.register(r"teams", TeamViewSet, basename="team")

urlpatterns = [
    path("", include(router.urls)),
    path("teams/", TeamViewSet.as_view({"post": "create"}), name="create-team"),
]
