from django.contrib import admin
from ddweb.apps.references.models import Reference, ReferenceImage

class ReferenceImageInline(admin.TabularInline):
    model = ReferenceImage
    extra = 3

class ReferenceAdmin(admin.ModelAdmin):
    inlines = [ReferenceImageInline]

admin.site.register(Reference, ReferenceAdmin)
