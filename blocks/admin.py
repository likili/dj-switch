from django.contrib import admin
from blocks.models import *

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ["name"]

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["menu", "name", "slug", "parent", "parent", "published", "ordering"]

    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Title)
admin.site.register(Snipet)