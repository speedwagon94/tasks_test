from rest_framework import generics, status
from django.db import models
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Subcategory, Product, Cart
from .pagination import PaginationClass
from .serializers import CategorySerializer, SubcategorySerializer, ProductSerializer, CartSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    """
    Представление для просмотра списка и создания категорий.

    - GET: Получение списка категорий.
    - POST: Создание новой категории.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для просмотра, обновления и удаления категории.

    - GET: Получение детальной информации о категории.
    - PUT, PATCH: Обновление информации о категории.
    - DELETE: Удаление категории.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryListCreateView(generics.ListCreateAPIView):
    """
    Представление для просмотра списка и создания подкатегорий.

    - GET: Получение списка подкатегорий.
    - POST: Создание новой подкатегории.
    """
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class SubcategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для просмотра, обновления и удаления подкатегории.

    - GET: Получение детальной информации о подкатегории.
    - PUT, PATCH: Обновление информации о подкатегории.
    - DELETE: Удаление подкатегории.
    """
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class ProductListCreateView(generics.ListCreateAPIView):
    """
    Представление для просмотра списка и создания продуктов.

    - GET: Получение списка продуктов с пагинацией.
    - POST: Создание нового продукта.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PaginationClass


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для просмотра, обновления и удаления продукта.

    - GET: Получение детальной информации о продукте.
    - PUT, PATCH: Обновление информации о продукте.
    - DELETE: Удаление продукта.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartListView(generics.ListCreateAPIView):
    """
    Представление для просмотра списка и создания элементов корзины пользователя.

    - GET: Получение списка элементов корзины пользователя.
    - POST: Добавление нового элемента в корзину пользователя.
    """
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для просмотра, обновления и удаления элемента корзины.

    - GET: Получение детальной информации об элементе корзины.
    - PUT, PATCH: Обновление информации об элементе корзины.
    - DELETE: Удаление элемента корзины.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartClearView(APIView):
    """
    Представление для очистки корзины пользователя.

    - POST: Очистка корзины пользователя.
    """
    def post(self, request):
        user = request.user
        Cart.objects.filter(user=user).delete()
        return Response({'message': 'Cart cleared successfully'}, status=status.HTTP_200_OK)


class CartSummaryView(APIView):
    """
    Представление для получения сводки информации о корзине пользователя.

    - GET: Получение информации о количестве товаров, общей стоимости и списка элементов корзины пользователя.
    """
    def get(self, request):
        user = request.user
        cart_items = Cart.objects.filter(user=user)

        total_quantity = cart_items.aggregate(total_quantity=models.Sum('quantity'))['total_quantity'] or 0
        total_cost = sum(item.product.price * item.quantity for item in cart_items)

        response_data = {
            'total_quantity': total_quantity,
            'total_cost': total_cost,
            'cart_items': CartSerializer(cart_items, many=True).data
        }

        return Response(response_data)
