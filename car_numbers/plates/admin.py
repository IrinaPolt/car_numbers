from django.contrib import admin

from .models import Plate


@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')
    search_fields = ('number', )
