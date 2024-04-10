from django.urls import path
from .views import *

app_name = 'techhive'

urlpatterns = [
    path('', techHiveHome_view, name='techhivehome'),
]