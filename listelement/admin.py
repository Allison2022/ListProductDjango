from django.contrib import admin

# Register your models here.
from listelement.models import Category, Type, Element

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_clean')

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_clean')

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_clean', 'description', 'category', 'type')