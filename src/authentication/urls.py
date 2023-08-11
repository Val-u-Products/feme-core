from django.urls import path, include
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
# from .views import LoginView, LogoutView, SignupView
from .views import CustomLoginView

# urlpatterns = [
#     path('auth/login/',
#          LoginView.as_view(), name='auth_login'),
#     path('auth/logout/',
#          LogoutView.as_view(), name='auth_logout'),
#     path('auth/signup/',
#          SignupView.as_view(), name='auth_signup'),
# ]
urlpatterns = [
    path("register/", RegisterView.as_view(), name="rest_register"),
    # path("login/", LoginView.as_view(), name="rest_login"),
    path("login/", CustomLoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
]
