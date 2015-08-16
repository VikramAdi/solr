from django.contrib import admin
from shop.models import Shop
# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    ordering=['name']
    filter_horizontal  = ['delivery_areas','served_categories','products',]

admin.site.register(Shop,ShopAdmin)