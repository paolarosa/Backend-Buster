from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from .serializers import UserSerializer
from .models import User
from .serializers import CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import MyCustomPermission, EmployeeAndOwner
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 201)

class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer

class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, EmployeeAndOwner]
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def patch(self, request, user_id):
        user=get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
