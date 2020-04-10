from django.contrib import admin

from .models import Property , Category, Reserve

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name','type','price','category','location','beds_number','baths_number','garages_number']
    search_fields = ['location','type']
    list_filter = ['category','type']


admin.site.register(Property, PropertyAdmin)
admin.site.register(Category)
admin.site.register(Reserve)
