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
    # return os.path.join("images", filename)
    return "%s/%s" % (settings.MEDIA_ROOT, filename)

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


class Free_minds(models.Model):
    title_mds = models.CharField(verbose_name=u'Заголовок:', max_length=255, null=True, blank=True)
    slug = models.CharField(verbose_name=u'Url:', max_length=255, blank=True)
    desc_text = models.CharField(verbose_name="Подзаголовок", max_length=355, null=True, blank=True)
    full_textt = models.TextField(verbose_name="Подробное описание", null=True, blank=True)
    image = models.ImageField(upload_to=get_file_path, blank=True, verbose_name="Логотип", null=True)
    published = models.BooleanField(verbose_name="Опубликовано", default=0)
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)


    def __str__(self):
        return self.title_mds

    class Meta:
        verbose_name_plural = "Преимущества"
        verbose_name = "Преимущество"

# class Block_2(models.Model):
#     title_block = models.CharField(verbose_name=u'Заголовок:', max_length=255)
#     desc_text = models.CharField(verbose_name="Подзаголовок", max_length=355)
#     # image = models.ImageField(upload_to=get_file_path, blank=True, verbose_name="Логотип")
#     published = models.BooleanField(verbose_name="Опубликовано", default=0)
#     blc_position = models.ForeignKey(Free_minds, on_delete=models.CASCADE, null=True, blank=True,verbose_name="Блоки:")
#
#     def __str__(self):
#         return self.title_block
#
#     class Meta:
#         verbose_name_plural = "Блок 2"

class Title(models.Model):
    title = models.CharField(verbose_name=u'Оффер:', max_length=255)
    image = models.ImageField(upload_to=make_upload_path, blank=True, verbose_name="Логотип")
    background = models.ImageField(upload_to=make_upload_path, blank=True, verbose_name="Изображение")
    published = models.BooleanField(verbose_name="Опубликовано", default=0)
    title_blck2 = models.CharField(verbose_name=u'Заголовок:', max_length=255, null=True)
    desc_text_blck2 = models.CharField(verbose_name="Подзаголовок", max_length=355, null=True)
    # image = models.ImageField(upload_to=get_file_path, blank=True, verbose_name="Логотип")
    blck_position = models.ManyToManyField(Free_minds, verbose_name="Преимущества:")


    def get_result(self):
        return Results.objects.filter(category=self) # вернет нам список тайтлов где будут совпадать значения и заголовки фраз

    def image_img(self):
        if self.image:
            return u'<img src="%s" width="70" />' % self.image.url
        else:
            return '(none)'

    image.short_description = 'Thumb'
    image.allow_tags = True


    def __str__(self):
        return self.title



    class Meta:
        verbose_name_plural = "Офферы"
        verbose_name = "Оффер"

# подзаголовки на главной страницы
class Results(models.Model):
    category = models.ForeignKey(Title, blank=True, null=True, verbose_name="Категории")
    str1 = models.CharField(verbose_name=u'Строка 1:', max_length=255, null=True, blank=True)
    str1 = models.CharField(verbose_name=u'Строка 1:', max_length=255, null=True, blank=True)
    str1 = models.CharField(verbose_name=u'Строка 1:', max_length=255, null=True, blank=True)
# в шаблоне надо прописать так мы будем получать динамичные заголовки:
# {% for i in object.get_result %}
#     <p>{{i.str1}}<span class="yellwords">{{i.str2}}</span>{{i.str3}}</p>
# {% endfor %}





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