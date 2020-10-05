from django.contrib import admin

from .models import Realtor
# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_mvp','email','hire_date',)
    list_display_links = ('id','name',)
    list_editable = ('is_mvp',)
    search_fields = ('name','email')

admin.site.register(Realtor,RealtorAdmin)
