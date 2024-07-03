from django.urls import path
from .views import (HomeView, LoginView, ContactView,
                    PasswordResetView, RegisterView, NotFoundView)

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('register/', RegisterView.as_view(), name='register'),
    path('notfound/', NotFoundView.as_view(), name='notfound'),
]