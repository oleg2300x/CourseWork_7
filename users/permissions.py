from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Провека владельца"""
    message = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsUser(BasePermission):
    """Проверка владельца"""
    message = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        return request.user == obj
