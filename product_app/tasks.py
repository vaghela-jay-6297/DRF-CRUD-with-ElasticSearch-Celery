# product_app/tasks.py
from celery import shared_task
from elasticsearch import Elasticsearch
from .models import Product
from .documents import ProductDocument

@shared_task
def add_product_to_elasticsearch(product_id):
    product = Product.objects.get(id=product_id)
    product_doc = ProductDocument(
        meta={'id': product.id},
        id=product.id,
        name=product.name,
        description=product.description
    )
    product_doc.save()

@shared_task
def update_product_in_elasticsearch(product_id):
    product = Product.objects.get(id=product_id)
    product_doc = ProductDocument.get(id=product.id)
    product_doc.name = product.name
    product_doc.description = product.description
    product_doc.save()

@shared_task
def delete_product_from_elasticsearch(product_id):
    product_doc = ProductDocument.get(id=product_id)
    product_doc.delete()

@shared_task
def search_elasticsearch(query):
    es = Elasticsearch()
    # Implement Elasticsearch search query here
    # Example:
    search_result = es.search(index='product_index', body={'query': {'match': {'name': query}}})
    return search_result
