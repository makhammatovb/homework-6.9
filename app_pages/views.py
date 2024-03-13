from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


links = f"<ul><li><a href='/themes/'>Themes</a></li><li><a href='/pupils/'>Pupils</a></li></ul>"

def index(request):
    return HttpResponse("<h1>Index Page</h1>" + links)

def about(request):
    html = "<h1>About Page</h1>"
    html += links
    return HttpResponse(html)

def contact(request):
    html = "<h1><a href='tel:+9989999999'>Contact</a></h1>"
    html += links
    return HttpResponse(html)

def themes(request):
    html = "<h1>List of Themes Page</h1>"
    html += links
    return HttpResponse(html)

def pupils(request):
    html = "<h1>Pupils Page</h1>"
    html += links
    return HttpResponse(html)
