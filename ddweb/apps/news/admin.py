from django.contrib import admin
from ddweb.apps.news.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'date', 'description', 'author', 'image_admin_url')

    def image_admin_url(self, obj):
        return '<a href="/images/uploadf/article/%s">Upload images</a>' % obj.id
    image_admin_url.allow_tags = True

admin.site.register(Article, ArticleAdmin)
