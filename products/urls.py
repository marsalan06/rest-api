from .import views
from django.urls import path

urlpatterns = [
    path('products/',views.products_list),
    path('products/<int:pk>/',views.product_detail),
]
