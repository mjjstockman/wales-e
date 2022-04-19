from django.urls import path
from . import views

urlpatterns = [
    path('', views.createSetlist, name='create-setlist'),
    path('update-setlist/<str:pk>', views.updateSetlist, name='update-setlist'),
]