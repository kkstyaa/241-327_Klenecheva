import random
import string
import datetime
from .models import Book
from django.db import transaction, connection

def gentestdata():
    with connection.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE mainapp_book RESTART IDENTITY;")
    with transaction.atomic():
        
        for i in range(1000):
            book = Book()
            book.published_date = datetime.date(
                random.randint(2000, 2024),
                random.randint(1, 12),
                random.randint(1, 28)
            )
            book.is_available = random.random() > 0.3
            
            book.title = random.choice([
                'Война и мир', 
                'Преступление и наказание', 
                'Мастер и Маргарита', 
                'Анна Каренина',
                'Идиот',
                'Отцы и дети',
                'Тихий Дон',
                'Собачье сердце',
                'Мертвые души',
                'Евгений Онегин'
            ])
            
            book.author = random.choice([
                'Толстой Л.Н.',
                'Достоевский Ф.М.',
                'Булгаков М.А.',
                'Чехов А.П.',
                'Тургенев И.С.',
                'Шолохов М.А.',
                'Гоголь Н.В.',
                'Пушкин А.С.',
                'Лермонтов М.Ю.',
                'Солженицын А.И.'
            ])
            
            isbn = ''
            for _ in range(13):
                isbn += str(random.randint(0, 9))
            book.isbn = isbn
            
            book.save()
            
            if (i + 1) % 100 == 0:
                print(f'Создано {i + 1} книг...')
    
    print('OK gentestdata()')