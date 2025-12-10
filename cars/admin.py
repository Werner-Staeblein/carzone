from django.contrib import admin
from cars.models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_title', 'color', 'model', 'year', 'body_style', 'is_featured')
    list_display_links = ('id', 'car_title')
    list_editable = ('is_featured',)
    seearch_fields = ('id', 'city', 'model')
    list_filter = ['city', 'model', 'body_style']

admin.site.register(Car, CarAdmin)

