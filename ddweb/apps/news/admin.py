from django import forms
from django.contrib import admin
from django.db import models
from ddweb.apps.news.models import Article, ArticleImage

class ArticleImageForm(forms.ModelForm):
    class Meta:
        model = ArticleImage
        fields = ['image', 'caption']
        widgets = {
        }

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageInline]

admin.site.register(Article, ArticleAdmin)
