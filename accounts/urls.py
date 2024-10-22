from django.urls import path, include
from django.contrib.auth import views
from .views import CustomUserCreateView

urlpatterns = [
    path('register/', CustomUserCreateView.as_view(), name='reg'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]
