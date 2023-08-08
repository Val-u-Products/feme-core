"""
URL configuration for feme_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from core.views import actualizar_key
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers # new line
router = routers.DefaultRouter() # new line
from core.views import LoginAPIView, SalonInfoProfeAPIView, TopStudentsAPIView, InfoProfeView, ProgresoView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', LoginView.as_view(), name="login"),
    # path('logout/', logout_view, name="logout"),
    # path('register/', UserRegistration.as_view(), name='user_registration'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('monitortabla/<int:pk>/actualizar_key/', actualizar_key, name='actualizar_key'),
    path('', include('core.urls')),
    path('api/auth/', include('authentication.urls')), # new line
    path('api/', include(router.urls)), # new line
    path('login_token/', LoginAPIView.as_view(), name='login_token'),
    path('salon_info_profe/', SalonInfoProfeAPIView.as_view(), name='salon_info_profe'),
    path('top_students/', TopStudentsAPIView.as_view(), name='top_students'),
    path('info-profe/', InfoProfeView.as_view(), name='info-profe-view'),
    path('progreso/', ProgresoView.as_view(), name='progreso-list'),
]
