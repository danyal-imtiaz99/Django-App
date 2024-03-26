from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Website for Meeting planner")

# Add something about yourself on the page!

def about(request):
    return HttpResponse("Hi there, my name is Danyal and I'm building a web app for meeting planner using Django!")