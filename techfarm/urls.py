from django.contrib import admin
from django.urls import path, include
from main.views import home_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home_view, name='home'),
    path("admin/", admin.site.urls),
    path('account/', include('account.urls')),
    path('main/', include('main.urls')),
    path('farmhive/', include('farmhive.urls')),
    path('techhive/', include('techhive.urls')),
    path('payment/', include('payment.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)