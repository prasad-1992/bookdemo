from rest_framework import serializers
from .models import BookSale

class BookSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSale
        fields = ['id', 'book', 'sale_date', 'quantity']
