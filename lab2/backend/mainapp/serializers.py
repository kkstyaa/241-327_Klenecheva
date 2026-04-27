from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    Преобразует объекты Book в JSON и обратно.
    """
    class Meta:
        model = Book
        fields = '__all__'  # все поля модели
    