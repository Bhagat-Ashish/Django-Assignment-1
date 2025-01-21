from django.urls import path
from .views import product_view

urlpatterns = [
    path('<str:category>/<int:product_id>/', product_view, name='product'),
]
