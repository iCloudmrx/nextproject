from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass
