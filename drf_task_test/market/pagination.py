from rest_framework.pagination import PageNumberPagination


class PaginationClass(PageNumberPagination):
    """
    Класс для настройки пагинации в Django REST Framework.

    Attributes:
    - page_size (int): Количество элементов на одной странице по умолчанию.
    - page_size_query_param (str): Название параметра запроса для изменения размера страницы.
    - max_page_size (int): Максимальное количество элементов на странице, которое разрешено.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
