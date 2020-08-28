from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_site, name='base_site'),
    path('upload/', views.upload, name='upload'),
]
