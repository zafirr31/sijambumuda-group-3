from .views import show_history
from django.urls import path

urlpatterns = [
    path('', show_history, name='show_history'),
]
