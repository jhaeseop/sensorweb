from django.urls import path
from . import views

urlpatterns = [
    path('picam/', views.picam, name='picam'),
]
