from django.contrib import admin
from .models import CustomUser, Product, Category, TypeOfPrice, ProductImage

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone_number', 'profile_photo', 'address')

admin.site.register(CustomUser, CustomUserAdmin)
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'articul', 'price', 'type_of_price', 'created_at', 'last_updated')
    list_display_links = ('id', 'name')
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Category, CategoryAdmin)

class TypeOfPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(TypeOfPrice, TypeOfPriceAdmin)