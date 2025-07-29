from django.contrib import admin
from . models import Category, Blog

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
class BlogAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    list_display = ('id', 'name', 'category', 'status')

admin.site.register(Category,CategoryAdmin)

admin.site.register(Blog),BlogAdmin



