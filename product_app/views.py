# product_app/views.py
from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .tasks import add_product_to_elasticsearch, update_product_in_elasticsearch, delete_product_from_elasticsearch, search_elasticsearch

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        add_product_to_elasticsearch.delay(instance.id)

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        update_product_in_elasticsearch.delay(instance.id)

    def perform_destroy(self, instance):
        delete_product_from_elasticsearch.delay(instance.id)

def search_product(request):
    query = request.query_params.get('q', '')
    result = search_elasticsearch.delay(query).get()
    return Response(result)
