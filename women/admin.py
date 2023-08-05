from django.contrib import admin
from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('cat','title','time_create','time_update','is_publish')
    list_display_links = ('title',)
    search_fields = ('title','cat')
    list_editable = ('is_publish',)
    list_filter = ('cat', 'is_publish')
    prepopulated_fields = {'slug':('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
