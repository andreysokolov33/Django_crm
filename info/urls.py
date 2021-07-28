from django.urls import path
from .views import *

app_name = 'info'

urlpatterns = [
    path('antennas/', antennas_list),
    path('operators/', operators),
    path('operators/create/', operator_create),
    path('operators/<int:pk>/', operator_details),
    path('operators/<int:pk>/update/', operator_update),
    path('operators/<int:pk>/delete/', operator_delete),
]
