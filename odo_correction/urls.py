from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_site, name='base_site'),
    path('info/', views.info, name='info'),
    path('excel/', views.excel_list, name='excel_list'),
    path('excel/upload/', views.excel_upload, name='excel_upload'),
    path('excel/<int:pk>/', views.excel_delete, name='excel_delete'),
    path('excel_correction/<int:pk>/', views.excel_correction, name='excel_correction'),
    path('error/', views.error, name='error'),
    
]
