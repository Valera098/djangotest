from django.contrib import admin

from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'contents')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)