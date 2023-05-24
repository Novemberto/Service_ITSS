from django.urls import path
from . import views

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('', views.getRoutes),
    path('users/', views.getUsers, name="users"),
    
    # path('users/<str:pk>/', views.getUser),
    
    path('users/<str:pk>/', views.GetUser.as_view()),
    
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]