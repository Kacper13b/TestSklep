from django.contrib import admin
from .models import Category, Product, ProductImage


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 5


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['name', 'slug', 'stock', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['stock', 'price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Product


admin.site.register(ProductImage)
