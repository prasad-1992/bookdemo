from django.urls import path
from .views import BookSaleListCreateView, BookSaleDeleteView, BookSaleSearchView, BookSaleSalesTrendsView

urlpatterns = [
    path('api/booksales/', BookSaleListCreateView.as_view(), name='booksale-list-create'),
    path('api/booksales/<int:pk>/', BookSaleDeleteView.as_view(), name='booksale-delete'),
    path('api/booksales/search/', BookSaleSearchView.as_view(), name='booksale-search'),
    path('api/booksales/sales-trends/<int:book_id>/', BookSaleSalesTrendsView.as_view(), name='booksale-sales-trends'),
]
