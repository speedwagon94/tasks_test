from rest_framework import serializers
from .models import Category, Subcategory, Product, Cart


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Category.

    Fields:
    - id (int): Уникальный идентификатор категории.
    - name (str): Название категории.
    - description (str): Описание категории.
    """
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Subcategory.

    Fields:
    - id (int): Уникальный идентификатор подкатегории.
    - category (CategorySerializer): Сериализатор для связанной категории.
    - name (str): Название подкатегории.
    - description (str): Описание подкатегории.
    """
    class Meta:
        model = Subcategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.

    Fields:
    - id (int): Уникальный идентификатор продукта.
    - subcategory (SubcategorySerializer): Сериализатор для связанной подкатегории.
    - name (str): Название продукта.
    - description (str): Описание продукта.
    - price (float): Цена продукта.
    """
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Cart.

    Fields:
    - id (int): Уникальный идентификатор записи корзины.
    - user (int): Идентификатор пользователя.
    - product_id (int): Идентификатор продукта в корзине.
    - quantity (int): Количество продукта в корзине.
    """
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product_id', 'quantity']
