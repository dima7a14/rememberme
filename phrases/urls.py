from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PhraseViewSet

router = DefaultRouter()

router.register(r"phrases", PhraseViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
