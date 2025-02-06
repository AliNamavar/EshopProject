from django.contrib import admin
from . import models


# Register your models here.
class footerLinkAdmin(admin.ModelAdmin):
    list_display = ["title", "url"]


class sliderLinkAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "is_active"]
    list_editable = ["is_active", "url"]


class site_banner_admin(admin.ModelAdmin):
    list_display = ["title", "url_title", "is_active", "position"]


admin.site.register(models.siteSettings)
admin.site.register(models.footerLink, footerLinkAdmin)
admin.site.register(models.footerLinkBox)
admin.site.register(models.slider, sliderLinkAdmin)
admin.site.register(models.site_banner, site_banner_admin)
