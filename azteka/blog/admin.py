from django.contrib import admin
from .models import Post, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    ordering = ('updated','created')
    search_fields = ('title', 'author__username', 'created')

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)