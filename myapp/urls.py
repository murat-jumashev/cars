from django.urls import path 
from . import views


app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index' ),
    path('cars/<int:pk>', views.car_details, name='car_details'),
    path('cars/<int:pk>/edit', views.car_edit, name='car_edit'),
    path('cars/<int:pk>/delete', views.car_delete, name='car_delete'),
]