from django.shortcuts import render, get_object_or_404
from .models import *

active_app = 'farm'

def home_view(request):
    home_contents = Home.objects.all()
    pictures = Pictures.objects.all()[:3]
    videos = VideoGellary.objects.all()[:3]
    departments = Departments.objects.all()[:5]
    return render(request, 'farm/index.html', {'departments': departments, 'videos': videos,
                        'home_contents': home_contents, 'pictures': pictures,'active_app': active_app})

# def about_view(request):
#     about_farmhive = AboutFarmHive.objects.all()
#     return render(request, 'farm/about.html', {'about': about_farmhive, 'active_app': active_app})

def gellary_view(request):
    gellary = VideoGellary.objects.all()[:5]
    pictures = Pictures.objects.all()[:5]
    return render(request, 'farm/gellary.html', {'gellary': gellary, 'pictures': pictures, 'active_app': active_app})

def galleryDetail_view(request):
    gellary = VideoGellary.objects.all()
    pictures = Pictures.objects.all()

    return render(request, 'farm/detail_gallery.html', {'gellary': gellary, 'pictures': pictures, 'active_app': active_app})

def digiFarms(request):
    digitalfarms = DigitalFarms.objects.all()

    return render(request, 'farm/digifarms.html', {'digitalfarms': digitalfarms, 'active_app': active_app})

def digiFarms_details(request, department_id):
    digitalfarms = get_object_or_404(DigitalFarms, pk=department_id)
    return render(request, 'farm/digifarms_details.html', {'digitalfarms': digitalfarms, 'active_app': active_app})