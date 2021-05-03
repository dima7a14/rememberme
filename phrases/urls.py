from django.urls import path, include
from rest_framework_nested import routers

from .views import PhraseViewSet, TranslationViewSet, MentionViewSet

router = routers.DefaultRouter()
router.register(r"phrases", PhraseViewSet)

phrases_router = routers.NestedDefaultRouter(router, r"phrases", lookup="phrase")
phrases_router.register(r"translations", TranslationViewSet, basename="phrase-translations")
phrases_router.register(r"mentions", MentionViewSet, basename="phrase-mentions")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(phrases_router.urls)),
]
