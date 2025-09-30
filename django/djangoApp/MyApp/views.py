from pyexpat.errors import messages
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth
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
            return redirect('login')
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

def login(request):
    messages = []
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Person.objects.get(email=email)
            if user.password == password:
                messages.append("Login successful!")
                # You can redirect to a dashboard or homepage here
                request.session['user_id'] = user.id
                return redirect('dashboard')
            else:
                messages.append("Invalid password.")
        except Person.DoesNotExist:
            messages.append("User with this email does not exist.")
    return render(request, "login.html", {'messages': messages})

def dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # if not logged in, redirect to login

    user = Person.objects.get(id=user_id)
    return render(request, "dashboard.html", {"user": user})

def logout(request):
    auth.logout(request)
    return redirect('login')