from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_member, name="register"),
    path('login/', login_member, name='login')
]
