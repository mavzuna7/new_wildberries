from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    name = models.CharField(
        verbose_name="Наименование",
        max_length=200,
        )
    desc = models.TextField(
        verbose_name="Описание",
        max_length=600,
        )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2,
        )
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="products/",
    )
    category = models.ForeignKey(
        "Category",
        verbose_name="Категория",
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        "Brand",
        verbose_name="Бренд",
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(
        verbose_name="URL (автоматически)",
        unique=True,
        null=True,
    )
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    
    def str(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=200,
    )
    parent = models.ForeignKey(
        "self",
        verbose_name="Родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        verbose_name="URL (автоматически)",
        unique=True,
        null=True,
        editable=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def str(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=200,
    )
    site_url = models.URLField(
        verbose_name="Ссылка на сайт",
        max_length=200,
    )
    country = models.CharField(
        verbose_name="Страна",
        max_length=200,
    )
    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    def str(self):
        return self.name