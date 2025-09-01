from django.urls import path
from . import views

urlpatterns = [
    path('downloads', views.index, name='index')
]