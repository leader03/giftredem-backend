from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from base.models import *
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework import filters
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


class CustomerTokenObtainPairView(TokenObtainPairView):
    permissions_classes = (AllowAny,)
    serializer_class = CustomerTokenObtainPairSerializer 

class CustomerRegisterView(generics.CreateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerRegisterSerializer

class LoginAuthView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if CustomerUser.objects.filter(user=request.user).exists():
                customer = CustomerUser.objects.get(user=request.user)
                serializer = CustomerUserSerializer(customer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif VendorUser.objects.filter(user=request.user).exists():
                vendor = VendorUser.objects.get(user=request.user)
                serializer = VendorUserSerializer(vendor)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)