from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', register_member, name="register"),
    path('', include('django.contrib.auth.urls')),
    path('check-username/', check_username, name="check-username"),
    path('check-email/', check_email, name="check-email"),
    path('check-password/', check_password, name="check-password"),
]
