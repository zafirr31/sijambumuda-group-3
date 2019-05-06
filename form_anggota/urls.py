from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', register_member, name="register"),
    path('auth/', include('social_django.urls', namespace='social')),
]
