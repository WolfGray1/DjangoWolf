from django.urls import path
from . import views
from .views import user_form_view
from .views import create_book, book_list, edit_book, delete_book

urlpatterns = [
    path('', views.home, name='home'),
    path('image/', views.image_view, name='image'),  # Проверяем, что это правильно прописано
    path('upload/', views.upload_image, name='upload_image'),
    path('media/<path:path>', views.media, name='media'),
    path('contact/', views.contact, name='contact'),
    path('user_form/', user_form_view, name='user_form'),
    path('books/', book_list, name='book_list'),
    path('books/add/', create_book, name='create_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]

