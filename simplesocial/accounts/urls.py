from django.urls import path
# to avoid mixing up views from contrib.auth and app views
# I'm importing contrib.auth as auth_views
from django.contrib.auth import views as auth_views

from . import views

app_name='accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
]