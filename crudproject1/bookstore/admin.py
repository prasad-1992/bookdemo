from django.contrib import admin
from .models import Book, BookSale

# Register your models here.
@admin.register(Book)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title','author')

@admin.register(BookSale)
class UserAdmin(admin.ModelAdmin):
    list_display = ('book','sale_date','quantity')