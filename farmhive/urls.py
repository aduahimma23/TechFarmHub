from django.urls import path
from .views import *

app_name = 'farm'

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('gellary/', gellary_view, name='gellary'),
    path('digiFarms<int:department_id>', digiFarms_details, name='digifarm_details'),
    path('digiFarms/', digiFarms, name='digifarm'),
    path('gallery_gallery/', galleryDetail_view, name='gellery_detail'),
]