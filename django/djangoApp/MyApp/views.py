from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.
def index(request):
    message = ""
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            Person.objects.create(name=name, email=email, password=password)
            message = "Registration successful!"
        except IntegrityError:
            message = "A user with this email already exists."
    return render(request, "index.html", {'message': message})

def counter(request):
    text = ""
    if request.method == "POST":
        text = request.POST.get('text', '')
    elif request.method == "GET":
        text = request.GET.get('text', '')
    text_count = len(text.split())
    return render(request, "counter.html", {'count': text_count})

def blog(request):
    return render(request, "blog.html")