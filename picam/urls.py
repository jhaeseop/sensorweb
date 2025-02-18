from django.urls import path
from . import views

urlpatterns = [
    path('picam/', views.picam, name='picam'),
    path('picam/data/', views.picam_data, name='picam_data'),  # JSON 데이터 반환 API
    path('webcam/', views.webcam, name='webcam'),
]
