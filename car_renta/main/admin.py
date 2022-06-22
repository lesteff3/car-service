from django.contrib import admin
from .models import Country, Auto, OrderItems, Brand


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'producing_country', )
    list_display_links = ('id', 'producing_country')
    search_fields = ('producing_country',)
    prepopulated_fields = {"slug": ("producing_country",)}


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'country', 'country_id')
    list_display_links = ('id', 'model', 'country')
    search_fields = ('model',)
    prepopulated_fields = {"slug": ('model',)}


class AutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'auto', 'brand', 'equpment', 'brand_id')
    list_display_links = ('id', 'auto', 'brand')
    search_fields = ('auto',)
    prepopulated_fields = {"slug": ('auto',)}


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'phone', 'color', 'status', 'created_at')
    list_display_links = ('id', 'order', 'product')
    search_fields = ('order',)


admin.site.register(Country, CountryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Auto, AutoAdmin)
admin.site.register(OrderItems, OrderItemsAdmin)

