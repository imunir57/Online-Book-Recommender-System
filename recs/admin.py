from django.contrib import admin
from .models import Book_list, Recommended_list

# Register your models here.
admin.site.register(Book_list)
admin.site.register(Recommended_list)