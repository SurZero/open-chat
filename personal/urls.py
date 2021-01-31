from django.urls import path
from .views import home

app_name = 'personal'

urlpatterns = [
    path('', home, name="home")
]
