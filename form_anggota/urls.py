from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', register_member, name="register"),
    path('', include('django.contrib.auth.urls')),
]
