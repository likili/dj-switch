from django.db import models

# Create your models here.

class Title(models.Model):
    title = models.CharField(verbose_name=u'Оффер:', max_length=255)

    def __str__(self):
        return self.title

class Block_2(models.Model):
    title = models.CharField(verbose_name=u'Заголовок 2 блока:', max_length=255)
    subtitle = models.CharField(verbose_name=u'Подзаголовок 2 блока:', max_length=255)

    def __str__(self):
        return self.title

class Block_3(models.Model):
    title = models.CharField(verbose_name=u'Заголовок 3 блока:', max_length=255)
    subtitle = models.CharField(verbose_name=u'Подзаголовок 3 блока:', max_length=255)

    def __str__(self):
        return self.title

class Block_4(models.Model):
    title = models.CharField(verbose_name=u'Заголовок 4 блока:', max_length=255)
    subtitle = models.CharField(verbose_name=u'Подзаголовок 4 блока:', max_length=255)

    def __str__(self):
        return self.title


class Block_5(models.Model):
    title = models.CharField(verbose_name=u'Заголовок 5 блока:', max_length=255)
    subtitle = models.CharField(verbose_name=u'Подзаголовок 5 блока:', max_length=255)

    def __str__(self):
        return self.title


class Block_5(models.Model):
    title = models.CharField(verbose_name=u'Заголовок 5 блока:', max_length=255)
    subtitle = models.CharField(verbose_name=u'Подзаголовок 5 блока:', max_length=255)

    def __str__(self):
        return self.title


class Block_6(models.Model):
    title = models.CharField(verbose_name=u'Заголовок 6 блока:', max_length=255)
    subtitle = models.CharField(verbose_name=u'Подзаголовок 6 блока:', max_length=255)

    def __str__(self):
        return self.title


class Block_71(models.Model):
    title = models.CharField(verbose_name=u'Заголовок 7.1 блока:', max_length=255)
    subtitle = models.CharField(verbose_name=u'Подзаголовок 7.1 блока:', max_length=255)

    def __str__(self):
        return self.title

class Block_72(models.Model):
    title = models.CharField(verbose_name=u'Заголовок 7.2 блока:', max_length=255)
    subtitle = models.CharField(verbose_name=u'Подзаголовок 7.2 блока:', max_length=255)

    def __str__(self):
        return self.title

class Block_73(models.Model):
    title = models.CharField(verbose_name=u'Заголовок 7.3 блока:', max_length=255)
    subtitle = models.CharField(verbose_name=u'Подзаголовок 7.3 блока:', max_length=255)

    def __str__(self):
        return self.title