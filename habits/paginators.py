from rest_framework.pagination import PageNumberPagination


class HabitsPagination(PageNumberPagination):
    """Пагинация для привычек"""
    page_size = 5
