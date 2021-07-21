from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(("phrases.urls", "phrases"), namespace="phrases")),
    path("api/schema.yml", SpectacularAPIView.as_view(), name="schema"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # path('api-auth/', include('rest_framework.urls')),
    path("", TemplateView.as_view(template_name="index.html")),
]
