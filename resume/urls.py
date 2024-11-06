from . import views
from django.urls import path
from .views import *

app_name = 'resume'

urlpatterns = [
     path('', views.index, name='index'),
]
