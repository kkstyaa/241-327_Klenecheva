"""
ASGI config for lab1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os #для работы с переменными окружения

from django.core.asgi import get_asgi_application #функция django, создающая asgi-приложение

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab1.settings')

application = get_asgi_application() #создает ASGI-приложение, которое будет обрабатывать запросы
