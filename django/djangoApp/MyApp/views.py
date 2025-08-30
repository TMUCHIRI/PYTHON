from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {
        'name': 'Timothy',
        'age': 24,
        'nationality': 'Brazilian',
    }
    return render(request, "index.html", context)
