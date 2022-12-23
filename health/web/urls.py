from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('screen/<id>', views.screen, name='screen'),
    path('testweb', views.testweb, name='testweb'),
] 