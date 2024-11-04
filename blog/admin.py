from PIL.PyAccess import mode_map
from django.contrib import admin
from .models import Category, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'views', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    readonly_fields = ('views',)

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
