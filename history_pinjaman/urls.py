from .views import show_history, history_json, profile
from django.urls import path

urlpatterns = [
    path('', show_history, name='show_history'),
    path('json/', history_json, name='history_json'),
    path('profile/', profile, name='profile')
]
