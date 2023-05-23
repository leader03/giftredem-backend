from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import * 

urlpatterns = [
    # path('', views.getData),
    # path('add/', views.addData)
    path('clogin/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('clogin/', CustomerTokenObtainPairView.as_view(), name="customer_token_obtain_pair"), 
    path('cregister/', CustomerRegisterView.as_view(), name='cregister'),
    path('logindata/',LoginAuthView.as_view(), name='login_data'),
]
