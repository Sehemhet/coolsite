from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('cat', 'get_html_photo', 'title','time_create','time_update','is_publish')
    list_display_links = ('title',)
    search_fields = ('title','cat')
    list_editable = ('is_publish',)
    list_filter = ('cat', 'is_publish')
    prepopulated_fields = {'slug':('title',)}

    fields = ('title','slug', 'cat', 'content', 'photo', 'get_html_photo', 'time_create', 'time_update','is_publish')
    readonly_fields = ('get_html_photo', 'time_create','time_update')
    def get_html_photo(self,object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50>')

    get_html_photo.short_description = 'Миниатюра'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.


admin.site.site_title = 'Админ-панель coolsite2'
admin.site.site_header = 'Админ-панель coolsite2'