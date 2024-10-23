from django.urls import path, include
from .views import main

app_name = 'main'


urlpatterns = [
    path('', main, name='main'),
]
