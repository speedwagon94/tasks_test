from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Модель для представления категорий продуктов.

    Fields:
    - name (str): Название категории.
    - slug (str): Уникальный слаг для категории в URL.
    - image (ImageField): Изображение категории.
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    """
    Модель для представления подкатегорий продуктов.

    Fields:
    - name (str): Название подкатегории.
    - slug (str): Уникальный слаг для подкатегории в URL.
    - image (ImageField): Изображение подкатегории.
    - parent_category (ForeignKey): Ссылка на родительскую категорию.
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='subcategory_images/')
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'parent_category')


class Product(models.Model):
    """
    Модель для представления продуктов.

    Fields:
    - name (str): Название продукта.
    - slug (str): Уникальный слаг для продукта в URL.
    - category (ForeignKey): Ссылка на категорию продукта.
    - subcategory (ForeignKey): Ссылка на подкатегорию продукта (может быть пустой).
    - price (DecimalField): Цена продукта.
    - image_1, image_2, image_3 (ImageField): Изображения продукта (необязательные).
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, null=True, blank=True, related_name='subproducts', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_1 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='product_images/', null=True, blank=True)


class Cart(models.Model):
    """
    Модель для представления корзины пользователя.

    Fields:
    - user (ForeignKey): Ссылка на пользователя, которому принадлежит корзина.
    - product (ForeignKey): Ссылка на продукт в корзине.
    - quantity (PositiveIntegerField): Количество продукта в корзине.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='carts')
    quantity = models.PositiveIntegerField()
