from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  #the path for our index view
    path('removeCity/<city_name>', views.removeCity, name='removeCity'),
]