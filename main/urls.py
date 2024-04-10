from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('news_list/', news_list, name='news_list'),
    path('news_list/<int:article_id>/', article_details, name='article_details'),
    path('projects/', project_list_view, name='project_list'),
    path('projects/<int:pk>/', project_details_view, name='project_detail'),
    path('search/', search_view, name='search'),
    path('team/', team_list_view, name='team'),
    path('team/<int:pk>/', team_details_view, name='team_detail'),
]