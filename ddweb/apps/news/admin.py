from django.contrib import admin
from ddweb.apps.news.models import Article, ArticleImage

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageInline]

admin.site.register(Article, ArticleAdmin)
