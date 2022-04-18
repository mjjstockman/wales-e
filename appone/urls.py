from django.urls import path
from . import views

urlpatterns = [
    path('', views.createSetlist, name='create_setlist'),
]