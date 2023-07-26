from django.shortcuts import render, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BookSale
from .serializers import BookSaleSerializer
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BookSale
# Create your views here.


from rest_framework import generics
from .models import BookSale
from .serializers import BookSaleSerializer

class BookSaleListCreateView(generics.ListCreateAPIView):
    queryset = BookSale.objects.all()
    serializer_class = BookSaleSerializer

class BookSaleDeleteView(generics.DestroyAPIView):
    queryset = BookSale.objects.all()

class BookSaleSearchView(APIView):
    def get(self, request):
        search_query = request.query_params.get('q', '')
        book_sales = BookSale.objects.filter(
            book__title__icontains=search_query
        ) | BookSale.objects.filter(
            book__author__icontains=search_query
        )
        serializer = BookSaleSerializer(book_sales, many=True)
        return Response(serializer.data)
    
class BookSaleSalesTrendsView(APIView):
    def get(self, request, book_id):
        sales_trends = BookSale.objects.filter(
            book_id=book_id
        ).annotate(
            month= models.functions.TruncMonth('sale_date')
        ).values(
            'month'
        ).annotate(
            total_quantity=Sum('quantity')
        ).values(
            'month', 'total_quantity'
        )
        return Response(sales_trends)