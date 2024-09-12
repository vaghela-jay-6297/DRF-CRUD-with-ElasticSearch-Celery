from dataclasses import field
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Product

@registry.register_document
class ProductDocument(Document):
    # add index related settings
    class Index:      
        name = "products"   # index name
        settings = {
            "number_of_shards": 1,  # primary shards of elastic search
            "number_of_replicas": 0 # copies of primary shards of elastic search(replicas)
        }

    class Django:
        model = Product     # pass models name
        field = ["name", "description"]        # add fields you want in elastic search





# from django_elasticsearch_dsl import Document, Index
# from .models import Product

# product_index = Index('products')

# @product_index.doc_type
# class ProductDocument(Document):
#     class Django:
#         model = Product  # Replace with your actual Django model

#         # Fields you want to index in Elasticsearch
#         fields = [
#             'id',
#             'name',
#             'description',
#             'price',
#             'quantity'
#         ]
