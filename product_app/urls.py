from django.urls import path
from product_app.views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, search_product

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('search/', search_product, name='product-search'),
]