from django.contrib import admin
from . import models
# Register your models here.

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_title', 'parent', 'is_active')
    list_editable = ['is_active', 'url_title', 'parent']

class Article(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'author')
    list_editable = ['is_active']

    def save_model(self, request, obj: models.Article, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_date', 'parent')



admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, Article)
admin.site.register(models.ArticleComments, ArticleAdmin)