from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('screen', views.screen, name='screen'),
    path('detectme', views.detectme, name='detectme'),
    path('testweb', views.testweb, name='testweb'),
    path('testweb2', views.testweb2, name='testweb2'),
] 