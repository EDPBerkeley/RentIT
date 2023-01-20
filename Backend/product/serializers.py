from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Class that serializes the Product Model so that
    it can be delivered in a json format
    """
    class Meta:
        model = Product

        fields = (
            'description',
            'pub_date',
            'price',
            'uuid'
        )
