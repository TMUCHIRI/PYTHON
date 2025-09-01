from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {
        'name': 'Timothy',
        'email': 'timothy@example.com',
        'password': 'Brazilian',
    }
    message = ""
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if name == context['name'] and email == context['email'] and password == context['password']:
            message = "Sign in successful!"
        else:
            message = "Sign in failed. Please check your credentials."
    return render(request, "index.html", {'message': message})
    