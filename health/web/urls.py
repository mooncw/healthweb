from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('screen', views.screen, name='screen'),
    path('detectme', views.detectme, name='detectme'),
] 