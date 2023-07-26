from django.test import TestCase
from django.test import TestCase, Client
from rest_framework import status
from .models import BookSale
from .serializers import BookSaleSerializer


# Test API Endpoints:
class BookSaleAPITestCase(TestCase):
    def setUp(self):
        # Set up sample book sales for testing
        self.client = Client()
        self.book1 = BookSale.objects.create(book_id=1, sale_date='2023-01-01', quantity=10)
        self.book2 = BookSale.objects.create(book_id=2, sale_date='2023-02-01', quantity=5)

    def test_list_book_sales(self):
        response = self.client.get('/api/booksales/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = BookSaleSerializer([self.book1, self.book2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_create_book_sale(self):
        data = {'book': 3, 'sale_date': '2023-03-01', 'quantity': 8}
        response = self.client.post('/api/booksales/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BookSale.objects.count(), 3)

    def test_delete_book_sale(self):
        response = self.client.delete(f'/api/booksales/{self.book1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BookSale.objects.count(), 1)


# Test Full-Text Search:
class BookSaleSearchTestCase(TestCase):
    def setUp(self):
        # Set up sample book sales for testing search
        self.client = Client()
        self.book1 = BookSale.objects.create(book_id=1, sale_date='2023-01-01', quantity=10)
        self.book2 = BookSale.objects.create(book_id=2, sale_date='2023-02-01', quantity=5)

    def test_search_book_sales(self):
        response = self.client.get('/api/booksales/search/?q=Book1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = BookSaleSerializer([self.book1], many=True).data
        self.assertEqual(response.data, expected_data)

        response = self.client.get('/api/booksales/search/?q=Author2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = BookSaleSerializer([self.book2], many=True).data
        self.assertEqual(response.data, expected_data)



# Test Graph Analytics:
class BookSaleSalesTrendsTestCase(TestCase):
    def setUp(self):
        # Set up sample book sales for testing sales trends
        self.client = Client()
        self.book1 = BookSale.objects.create(book_id=1, sale_date='2023-01-01', quantity=10)
        self.book2 = BookSale.objects.create(book_id=1, sale_date='2023-02-01', quantity=5)

    def test_sales_trends(self):
        response = self.client.get('/api/booksales/sales-trends/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['month'], '2023-01-01')
        self.assertEqual(response.data[0]['total_quantity'], 10)
        self.assertEqual(response.data[1]['month'], '2023-02-01')
        self.assertEqual(response.data[1]['total_quantity'], 5)


# Test Chart Rendering:
class BookSalesTemplateTestCase(TestCase):
    def test_chart_rendering(self):
        response = self.client.get('/book_sales/')  # Assuming the URL to the template is '/book_sales/'
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, '<canvas id="salesChart"></canvas>')
