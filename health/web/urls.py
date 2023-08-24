from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('screen/<id>', views.screen, name='screen'),
    # path('screen2/<id>', views.screen2, name='screen2')
    # path('index2', views.index2, name='index2'),
    # path('signup', views.signup, name='signup'),
    # path('login', views.login, name='login'),
] 