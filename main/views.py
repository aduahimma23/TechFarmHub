from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import *


def home_view(request):
    active_app = 'main'
    return render(request, 'main/index.html', {'active_app': active_app})

def contact_view(request):
    return render(request, 'main/contact.html')

def news_list(request):
    latest_news = NewsArticle.objects.order_by('-date_published')[:3]
    return render(request, 'news_list.html', {'latest_news': latest_news})

def article_details(request, article_id):
    articles = get_object_or_404(NewsArticle, pk=article_id)
    return render(request, 'article_details', {'articles': articles})

def project_list_view(request):
    projects = Projects.objects.all()
    return render(request, 'main/project_list', {'projects': projects})

def project_details_view(request, project_id):
    project_details = get_object_or_404(Projects, pk=project_id)
    return render(request, 'main/project_details', {'project_details': project_details})

def search_view(request):
    query = request.GET.get('q')
    results = Search.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'main/search_results.html', {'results': results})

def team_list_view(request):
    team_members = Team.objects.all()
    return render(request, 'main/team_list.html', {'teams': team_members})

def team_details_view(request, team_id):
    team_details = get_object_or_404(Team, pk=team_id)
    return render(request, 'main/team_details.html', {'team_details': team_details})