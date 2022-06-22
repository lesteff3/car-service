from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.country, name='rent'),
    path('<int:country_id>', views.detail, name='brand'),
    path('auto/<int:brand_id>', views.auto, name='auto'),
    path('auto_details/<int:pk>', views.AutoDetailView.as_view(), name='auto_detail'),
    path('rent_car/', views.register_rent_car, name='rent_car'),
    path('successful/', views.successful_register, name='successful')
    # path('<int:pk>', views.AutoDetailView.as_view(), name='auto')
]
