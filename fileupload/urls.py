from django.urls import path
from . import views

urlpatterns = [
    path('fileupload/', views.fileUpload, name='fileupload'),
]