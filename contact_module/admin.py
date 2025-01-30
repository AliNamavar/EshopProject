from django.contrib import admin
from . import models
# Register your models here.



class ContactAdmin(admin.ModelAdmin):
    list_display = ('title' ,'is_read_by_admin', 'created_date')
admin.site.register(models.Contact, ContactAdmin)