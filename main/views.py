from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *


def home_view(request):
    active_app = 'main'
    home_header = ChangeHeaderImages.objects.all()
    social = SocialMediaLinks.objects.all()
    footer = FooterArea.objects.all()
    partners = Partners.objects.all()
    projects = Projects.objects.all()[:5]

    return render(request, 'main/index.html', {'active_app': active_app, "home_header": home_header,
                "social": social, "footer": footer, "partners": partners, "projects": projects})

def contact_view(request):
    contact = ContactPage.objects.all()
    return render(request, 'main/contact.html', {"contact": contact})

def about_view(request):
    abouts = About.objects.all()
    return render(request, 'main/about.html', {'about': abouts})

def news_list(request):
    latest_news = NewsArticle.objects.order_by('-date_published')[:3]
    return render(request, 'news_list.html', {'latest_news': latest_news})

def article_details(request, article_id):
    articles = get_object_or_404(NewsArticle, pk=article_id)
    return render(request, 'article_details', {'articles': articles})

def project_list_view(request):
    projects = Projects.objects.all()
    project_header = ChangeProjectHeaderImage.objects.all()
    return render(request, 'main/project.html', {'projects': projects, 'project_image': project_header})

def project_details_view(request, project_id):
    project_details = get_object_or_404(Projects, pk=project_id)
    return render(request, 'main/project_details', {'project_details': project_details})

def service_view(request):
    services = Services.objects.all()
    # departments = Department.objects.all()[3]
    return render(request, 'main/services.html', {"services": services})

def search_view(request):
    query = request.GET.get('q')
    results = Search.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'main/search_results.html', {'results': results})

def team_list_view(request):
    members = Team.objects.all()
    return render(request, 'main/team_list.html', {'teams': members})

def team_details_view(request, team_id):
    members = get_object_or_404(Team, team_id=team_id)
    return render(request, 'main/team_details.html', {'team_members': members})

def galleryView(request):
    farms = FarmhiveGallery.objects.all()
    techs = TechhiveGallery.objects.all()
    multimedias = MultimediahiveGallery.objects.all()
    context = {"farms": farms, "techs": techs, "multimedias": multimedias}

    return render(request, 'main/gallery.html', context)

def techhiveView(request):
    techs = TechHive.objects.all()
    return render(request, 'main/tech_hive.html', {'techs': techs})

def multimediaView(request):
    multimedias = MultimediaHive.objects.all()
    return render(request, 'main/multimedia_hive.html', {'multimedias': multimedias})

def farmhiveView(request):
    farms = FarmHive.objects.all()
    return render(request, 'main/farm_hive.html', {'farms': farms})

@login_required
def buy_now(request, item_type, pk):
    item = None
    if item_type == 'tech':
        item = get_object_or_404(TechHive, pk=pk)
    elif item_type == 'multimedia':
        item = get_object_or_404(MultimediaHive, pk=pk)
    elif item_type == 'farm':
        item = get_object_or_404(FarmHive, pk=pk)

    if item:
        request.session['selected_item'] = {'type': item_type, 'pk': pk}
        return redirect('main:details')
    else:
        raise ValueError("No Item selected to proceed with the payment")