from django.urls import path
from . import views

urlpatterns = [
    path('auth', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('blog', views.blog, name='blog'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),

]