from django.contrib import admin
from blocks.models import *

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ["name"]

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["menu", "name", "slug", "parent", "parent", "published", "ordering"]

    prepopulated_fields = {'slug': ('name',)}

class Free_mindsAdmin(admin.ModelAdmin):
    list_display = ["title_mds", "published", "slug", "ordering"]

    prepopulated_fields = {'slug': ('title_mds',)}


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Free_minds, Free_mindsAdmin)
admin.site.register(Title)
admin.site.register(Snipet)