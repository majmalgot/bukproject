# bukapp/admin.py
from django.contrib import admin
from .models import Book



class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'price', 'publication_date']  
    search_fields = ('title', 'author')
    
admin.site.register(Book, BookAdmin)
