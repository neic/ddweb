from django.contrib import admin
from ddweb.apps.references.models import Reference


class ReferenceAdmin(admin.ModelAdmin):
    list_display = (
        "ship",
        "year",
        "description",
        "ongoing",
        "beforeDD",
        "image_admin_url",
    )

    def image_admin_url(self, obj):
        return '<a href="/images/uploadf/reference/%s">Upload images</a>' % obj.id

    image_admin_url.allow_tags = True


admin.site.register(Reference, ReferenceAdmin)
