from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_site, name='base_site'),
    #path('upload/', views.upload, name='upload'),
    path('info/', views.info, name='info'),
    path('excle/', views.excle_list, name='excle_list'),
    path('excle/upload/', views.excle_upload, name='excle_upload'),
    path('excle/<int:pk>/', views.excle_delete, name='excle_delete'),
]
