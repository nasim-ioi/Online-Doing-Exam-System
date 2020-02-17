from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Questions)
admin.site.register(Examiner)

# @admin.register(Item)
# class ItemAdmin(models.ModelAdmin):
#     list_display = ('id', 'title' , 'category')#ino too khod menue admin neshoon mide
#     search_fields = ('title',)
#     fields = ('title' , 'description')
#     readonly_fields = ('title',)
#     list_filter = ('title','color')
