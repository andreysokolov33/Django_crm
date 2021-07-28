from django.urls import path
from .views import *

app_name = 'info'

urlpatterns = [
    path('antennas/', antennas_list, name='antennas_list'),
    path('operators/', operators, name='operators_list'),
    path('operators/create/', operator_create, name='operators_create'),
    path('operators/<int:pk>/', operator_details, name='operators_unique'),
    path('operators/<int:pk>/update/', operator_update, name='operators_update'),
    path('operators/<int:pk>/delete/', operator_delete, name='operators_delete'),
]
