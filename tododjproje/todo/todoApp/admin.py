from django.contrib import admin
from todoApp.models import *



class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        # 'created_at',
        # 'updated_at',
    ]



class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'is_active',
        'category',
        'slug'
    ]
    list_display_links = [
        'title',
    ]
    
class Form_pageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'full_name',
        'text'
    ]


admin.site.register(Category, CategoryAdmin),
admin.site.register(Todo, TodoAdmin)
admin.site.register(Form_page, Form_pageAdmin)
