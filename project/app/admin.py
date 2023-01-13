from django.contrib import admin
from app.models import Menu, TypeMenu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'type')
    exclude = ['level']

@admin.register(TypeMenu)
class TypeMenuAdmin(admin.ModelAdmin):
    pass