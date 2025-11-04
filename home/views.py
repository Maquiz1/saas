from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

# Create your views here.
def home_page_view(request, *args, **kwargs):
    my_title = "Home Page"
    html_template = """home/home.html"""
    queryset = PageVisit.objects.all()
    queryset_count = queryset.count()
    PageVisit.objects.create(path=request.path)
    context = {
        "title": my_title,
        "queryset": queryset,
        "queryset_count": queryset_count
    }
    return render(request, html_template, context)
