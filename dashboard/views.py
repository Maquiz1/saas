from django.shortcuts import render
from django.http import HttpResponse


def dashboard_page_view(request,*args, **kwargs):
    return HttpResponse("Welcome to the Dashboard Home Page")
# Create your views here.
