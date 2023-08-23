from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('screen/<id>', views.screen, name='screen'),
    path('testweb', views.testweb, name='testweb'),
    path('testweb2', views.testweb2, name='testweb2'),
    path('testweb3', views.testweb3, name='testweb3'),
    # path('signup', views.signup, name='signup'),
    # path('login', views.login, name='login'),
    # path('home', views.home, name='home'),
] 