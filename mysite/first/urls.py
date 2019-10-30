from django.urls import path

from . import views


urlpatterns = [
    path('register', views.index, name='index'),
    path('login', views.login, name='login'),
    path('detail', views.detail, name='detail'),

]