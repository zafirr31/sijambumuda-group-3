from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', register_member, name="register"),
    path('login/', login_member, name='login'),
    path('logout/', logout_member, name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
]
