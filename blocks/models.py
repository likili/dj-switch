from django.db import models
import random, uuid
from django.conf import settings
import datetime
from mptt.models import MPTTModel, TreeForeignKey #категория строиться деревом
import os
import PIL
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill


def get_file_path(self, filename):
    extension = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), extension)
    return os.path.join("images", filename)

# Create your models here.

def make_upload_path(instance, filename, prefix = False):
    # Предоопределение имени загружаемого файла
    n1 = random.randint(0, 10000)
    n2 = random.randint(0, 10000)
    n3 = random.randint(0, 10000)
    filename = str(n1)+"_"+str(n2)+"_"+str(n3) + '.jpg'
    return u"%s/%s" % (settings.FILE_UPLOAD_HANDLERS, filename)

class Menu(models.Model):
    name = models.CharField(verbose_name=u'Название:', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Меню"

class MenuItem(MPTTModel):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True,verbose_name="Меню")
    name = models.CharField(verbose_name=u'Название:', max_length=255)
    slug = models.CharField(verbose_name=u'Url:', max_length=255)
    full_text = models.TextField(verbose_name="Полное описаание:", blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, verbose_name=u'Родительский пункт меню:', null=True, blank=True, related_name='children')
    published = models.BooleanField(verbose_name="Опубликовано", default=0)
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Пункты меню"

    class MPTTMeta:
        order_insertion_by = ['name']

# Произвольные куски кода которые мы будем вставлять в разных частях сайта
class Snipet(models.Model):
    name = models.CharField(verbose_name=u'Название:', max_length=255)
    text = models.TextField(blank=True, verbose_name="Код снипета")
    published = models.BooleanField(verbose_name="Опубликовано", default=0)
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)
    # генератор url:
    # slug = models.CharField(verbose_name=u'Url:', max_length=255, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Снипеты"
        verbose_name = "Снипет"



class Title(models.Model):
    title = models.CharField(verbose_name=u'Оффер:', max_length=255)
    image = models.ImageField(upload_to=get_file_path, blank=True, verbose_name="Логотип")
    background = models.ImageField(upload_to=get_file_path, blank=True, verbose_name="Изображение")
    published = models.BooleanField(verbose_name="Опубликовано", default=0)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Офферы"
        verbose_name = "Оффер"

class Free_minds(models.Model):
    title = models.CharField(verbose_name=u'Заголовок:', max_length=255)
    desc_text = models.CharField(verbose_name="Подзаголовок", max_length=355)
    full_textt = models.TextField(verbose_name="Подробное описание")
    image = models.ImageField(upload_to=get_file_path, blank=True, verbose_name="Логотип")
    published = models.BooleanField(verbose_name="Опубликовано", default=0)

    def __str__(self):
        return self.title

class Block_2(models.Model):
    title = models.CharField(verbose_name=u'Заголовок:', max_length=255)
    desc_text = models.CharField(verbose_name="Подзаголовок", max_length=355)
    image = models.ImageField(upload_to=get_file_path, blank=True, verbose_name="Логотип")
    published = models.BooleanField(verbose_name="Опубликовано", default=0)
    blc_position = models.ForeignKey(Free_minds, on_delete=models.CASCADE, null=True, blank=True,verbose_name="Блоки:")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Блок 2"

class Photos_wrk(models.Model):
    name = models.CharField(verbose_name=u'Название работы:', max_length=255)
    image = models.ImageField(upload_to=get_file_path, blank=True, verbose_name="Фото")
    published = models.BooleanField(verbose_name="Опубликовано", default=0)

    def __str__(self):
        return self.name

class Design_wrk(models.Model):
    name = models.CharField(verbose_name=u'Название работы:', max_length=255)
    image = models.ImageField(upload_to=get_file_path, blank=True, verbose_name="Дизайн")
    published = models.BooleanField(verbose_name="Опубликовано", default=0)

    def __str__(self):
        return self.name

class Print_wrk(models.Model):
    name = models.CharField(verbose_name=u'Название работы:', max_length=255)
    image = models.ImageField(upload_to=get_file_path, blank=True, verbose_name="Полиграфия")
    published = models.BooleanField(verbose_name="Опубликовано", default=0)

    def __str__(self):
        return self.name

class Category_wrk(models.Model):
    blc_pht = models.ForeignKey(Photos_wrk, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Фото:")
    blc_dsgn = models.ForeignKey(Design_wrk, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Дизайн:")
    blc_prnt = models.ForeignKey(Print_wrk, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Полиграфия:")


class Block_3(models.Model):
    title = models.CharField(verbose_name=u'Заголовок:', max_length=255)
    desc_text = models.CharField(verbose_name="Подзаголовок", max_length=355)
    published = models.BooleanField(verbose_name="Опубликовано", default=0)
    blc_ctgr = models.ForeignKey(Category_wrk, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Полиграфия:")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Блок 3"

class Comments(models.Model):
    name = models.CharField(verbose_name=u'Имя фамилие:', max_length=255)
    position = models.CharField(verbose_name=u'Должность:', max_length=255)
    text = models.TextField(blank=True, verbose_name="Код снипета")
    published = models.BooleanField(verbose_name="Опубликовано", default=0)
    image = models.ImageField(upload_to=get_file_path, blank=True, verbose_name="Фото:")

    def __str__(self):
        return self.name

class Block_4(models.Model):
    title = models.CharField(verbose_name=u'Заголовок:', max_length=255)
    desc_text = models.CharField(verbose_name="Подзаголовок", max_length=355)
    published = models.BooleanField(verbose_name="Опубликовано", default=0)
    blc_ctgr = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Комментарии:")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Блок 4"


class Block_5(models.Model):
    title = models.CharField(verbose_name=u'Заголовок:', max_length=255)
    desc_text = models.CharField(verbose_name="Подзаголовок", max_length=355)
    published = models.BooleanField(verbose_name="Опубликовано", default=0)
    image = models.ImageField(upload_to=get_file_path, blank=True, verbose_name="Логотип:")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Блок 5"

class Commands(models.Model):
    name = models.CharField(verbose_name=u'Имя фамилие:', max_length=255)
    links = models.CharField(verbose_name=u'Ссылка на профиль:', max_length=255)
    published = models.BooleanField(verbose_name="Опубликовано", default=0)
    image = models.ImageField(upload_to=get_file_path, blank=True, verbose_name="Фото:")

    def __str__(self):
        return self.name

class Block_6(models.Model):
    title = models.CharField(verbose_name=u'Заголовок:', max_length=255)
    desc_text = models.CharField(verbose_name="Подзаголовок", max_length=355)
    published = models.BooleanField(verbose_name="Опубликовано", default=0)
    blc_ctgr = models.ForeignKey(Commands, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Комментарии:")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Блок 4"






#
# class Block_71(models.Model):
#     title = models.CharField(verbose_name=u'Заголовок 7.1 блока:', max_length=255)
#     subtitle = models.CharField(verbose_name=u'Подзаголовок 7.1 блока:', max_length=255)
#
#     def __str__(self):
#         return self.title
#
# class Block_72(models.Model):
#     title = models.CharField(verbose_name=u'Заголовок 7.2 блока:', max_length=255)
#     subtitle = models.CharField(verbose_name=u'Подзаголовок 7.2 блока:', max_length=255)
#
#     def __str__(self):
#         return self.title
#
# class Block_73(models.Model):
#     title = models.CharField(verbose_name=u'Заголовок 7.3 блока:', max_length=255)
#     subtitle = models.CharField(verbose_name=u'Подзаголовок 7.3 блока:', max_length=255)
#
#     def __str__(self):
#         return self.title