from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

def index(request):
    return render(request, 'product/index.html')

class ProductView(viewsets.ViewSet):

    def index(self, request):
        return render(request, 'product/index.html')

    def get_all(self, request):
        products = Product.objects.all()
        serialized_products = ProductSerializer(products, many=True)
        return Response({"products": serialized_products.data})

    def get_product(self, request, uuid):
        product = Product.objects.get(uuid=uuid)
        serialized_product = ProductSerializer(product)
        return Response({"product": serialized_product.data})


