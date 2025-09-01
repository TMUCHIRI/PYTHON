from django.urls import path
from . import views

urlpatterns = [
    path('auth', views.index, name='index'),
    path('counter', views.counter, name='counter')

]