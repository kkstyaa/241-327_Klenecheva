from django.contrib import admin
from django.urls import path
from mainapp.views import BookViewSet
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    #cписок книг и создание новой
    path('books', BookViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    #hабота с конкретной книгой
    path('books/<int:pk>', BookViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]
