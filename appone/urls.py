from django.urls import path
from . import views

urlpatterns = [
    path('create-setlist/', views.createSetlist, name='create-setlist'),
    path('', views.setlist, name='setlist'),
    path('update-setlist/<str:pk>/', views.updateSetlist, name='update-setlist'),
    path('delete-setlist/<str:pk>/', views.deleteSetlist, name='delete-setlist'),
]