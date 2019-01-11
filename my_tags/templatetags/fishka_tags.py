# теги храним в папке templates
# ерархия в проекте созадем
# 'my_tags'
# |-templatetags
# |--name_tag.py
# INSTALLED_APPS = ['my_tags']

from django import template
register = template.Library()

from django.shortcuts import render, redirect, get_object_or_404
from blocks.models import Snipet
# верхний регистр

def my_app_name(app_name):
    try:
        app = __import__(app_name.lower())
        return app.app_label
    except:
        return app_name

my_app_name = register.simple_tag(my_app_name)

@register.filter
def lang(value):
    value=str(value)
    parts= value.split("/")
    return "/".join(parts[2:])

@register.filter
def fw(value):
    value= unicode(value)
    parts= value.split(" ")
    n = "<span>" + parts[0] + "</span>"
    a = " ".join(parts[1:])
    return n + a

@register.inclusion_tag("tags/top_menu.html")
def top_menu():
    from blocks.models import MenuItem, Menu
    menu = Menu.objects.get(pk=1)
    items = MenuItem.objects.filter(menu=menu, published=1).order_by("ordering")
    return {'items': items}



@register.inclusion_tag("tags/snip.html")
def snip(id):
    data = get_object_or_404(Snipet, pk=int(id))
    return {'data':data}
    # return "bob"



#
# @register.inclusion_tag("tags/snip2.html")
# def snip2(id):
#     data = get_object_or_404(Snipet, pk=int(id))
#     return {'data' : data}
#
# @register.inclusion_tag("tags/snip_img.html")
# def snip_img(id):
#     data = get_object_or_404(Snipet, pk=int(id))
#     return {'data' : data}
#
#
