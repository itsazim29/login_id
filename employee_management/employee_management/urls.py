from django.contrib import admin
from django.urls import path
from authentication.views import login_view, register_view  # Import your views
from django.views.generic import RedirectView  # Import for redirecting

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', login_view, name='login'),  # URL for login
    path('auth/register/', register_view, name='register'),  # URL for registration
    path('', RedirectView.as_view(url='/auth/login/')),  # Redirect root URL to login
]
