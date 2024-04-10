from django.urls import path
from .views import RegisterView, LoginView

app_name = 'account'

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login')
]