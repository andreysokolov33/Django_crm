from django.urls import path
from .views import *

app_name = 'info'

urlpatterns = [
    path('antennas/', antennas_list, name='antennas_list'),
    path('operators/', OperatorsListView.as_view(), name='operators_list'),
    path('operators/create/', OperatorsCreateView.as_view(), name='operators_create'),
    path('operators/<int:pk>/', OperatorsDetailView.as_view(), name='operators_unique'),
    path('operators/<int:pk>/update/', OperatorsUpdateView.as_view(), name='operators_update'),
    path('operators/<int:pk>/delete/', OperatorsDeleteView.as_view(), name='operators_delete'),
]
