from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'web/home.html')#HttpResponse("Hello")
	
def contact(request):
    return render(request, 'web/contact.html')#HttpResponse("Hello")

def projects(request):
    return render(request, 'web/notfound.html')#HttpResponse("Hello")

def blog(request):
    return render(request, 'web/notfound.html')#HttpResponse("Hello")

