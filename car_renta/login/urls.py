from django.urls import path, include


from login.views import signup, activate

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', signup, name='register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate'),

]