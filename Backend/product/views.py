from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductView(viewsets.ViewSet):
    """
    Class that contains routes/views for Product Objects
    """

    def index(self, request):
        """
        Landing page for product app
        """
        return render(request, 'product/index.html')

    def get_all(self, request):
        """
        Endpoint to get all product objects
        """
        products = Product.objects.all()
        serialized_products = ProductSerializer(products, many=True)
        return Response({"products": serialized_products.data})

    def get_product(self, request, uuid):
        """
        Endpoint to get single product object via uuid
        """
        product = Product.objects.get(uuid=uuid)
        serialized_product = ProductSerializer(product)
        return Response({"product": serialized_product.data})


