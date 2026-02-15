from django.contrib import admin
from .models import Category, Product, Order, OrderItem, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("name",)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "is_paid", "created_at")
    list_filter = ("is_paid",)
    inlines = [OrderItemInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "user", "rating", "created_at")
    list_filter = ("rating",)
    search_fields = ("comment",)
