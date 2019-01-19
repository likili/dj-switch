from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget

from blocks.models import *
from django.db import models


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ["name"]

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["menu", "name", "slug", "parent", "parent", "published", "ordering"]

    prepopulated_fields = {'slug': ('name',)}

class Free_mindsAdmin(admin.ModelAdmin):
    list_display = ["title_mds", "published", "slug", "ordering"]

    prepopulated_fields = {'slug': ('title_mds',)}

class TitleAdmin(admin.ModelAdmin):
    list_display = ["title",  "title_blck2",  "published"]
    fields = ["title",  "image", "image_img",  "background",  "published",  "title_blck2", "blck_position"]


admin.site.register(Image)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Free_minds, Free_mindsAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Snipet)