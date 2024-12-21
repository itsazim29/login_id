from django.urls import path
from .views import login_view, register_view  # Import the views from the current app

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
