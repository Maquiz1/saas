from django.urls import path,include
from dashboard.views import dashboard_page_view


app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_page_view, name='dashboard_view'),
]
