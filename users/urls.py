from django.urls import path
from rest_framework_simplejwt import views
from .views import UserView
from .views import LoginJWTView
from .views import UserDetailView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", views.TokenObtainPairView.as_view()),
    path("token/refresh/", views.TokenRefreshView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view())
]

