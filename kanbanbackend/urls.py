"""
URL configuration for kanbanbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from user.views import UserByTokenView
from user.routes import router as user
from kanban.routes import router as kanban

urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", SpectacularAPIView.as_view(), name="docs"),
    path(
        "docs/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="docs"),
        name="swagger-ui",
    ),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/user/", UserByTokenView.as_view(), name="token_user"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="docs"), name="redoc"),
    path("api-auth/", include("rest_framework.urls")),
    path("", include(user.urls)),
    path("", include(kanban.urls)),
]
