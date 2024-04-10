from django.shortcuts import render


def techHiveHome_view(request):
    return render(request, 'techhive/index.html')