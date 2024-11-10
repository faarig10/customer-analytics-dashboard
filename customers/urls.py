from django.urls import path
from . import views

urlpatterns = [
    path('api/customers/', views.customer_data_view, name='customer_data'),
    path('api/segmentation/', views.customer_segmentation_view, name='customer_segmentation'),
]
