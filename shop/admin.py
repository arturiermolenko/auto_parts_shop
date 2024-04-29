from django.contrib import admin
from .models import Item, Category, ItemImage


class ItemImageInline(admin.TabularInline):
    model = ItemImage


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]


admin.site.register(Category)
