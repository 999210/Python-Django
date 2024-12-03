from django.urls import path
from . import views

urlpatterns = [
    path('import/', views.import_csv, name='import_csv'),
    path('data/', views.data_list, name='data_list'),
    path('visualize/', views.visualize_data, name='visualize_data'),
]
