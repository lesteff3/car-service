from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', include('login.urls')),
    path('rent/', include('main.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
