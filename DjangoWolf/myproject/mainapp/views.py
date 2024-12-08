from .forms import UploadImageForm
from django.http import HttpResponse
from .forms import (ContactForm)
from .forms import UserForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm


def home(request):
    context = {
        'title': 'Главная страница',
        'content': 'Добро пожаловать на главную страницу!'
    }
    return render(request, 'home.html', context)
def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            return render(request, 'mainapp/image.html', {'image': image})
    else:
        form = UploadImageForm()
    return render(request, 'upload.html', {'form': form})
def media(request, path):
    return HttpResponse(f"Запрашиваемый путь к медиафайлу: {path}")
def image_view(request):
    # Здесь вы можете отобразить страницу или загрузить изображения
    return render(request, 'mainapp/image.html')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Здесь можно добавить логику сохранения данных или отправки сообщения
            return render(request, 'thankyou.html', {'name': name})
        else:
             # В случае ошибки форма будет отправлена обратно с сообщением об ошибке
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Категория пользователя по возрасту
            if age < 18:
                category = "Подросток"
            elif 18 <= age <= 60:
                category = "Взрослый"
            else:
                category = "Пожилой"
            return render(request, 'result.html', {
                'name': name,
                'email': email,
                'age': age,
                'category': category,
            })
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})
# Список книг
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Создание книги
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

# Редактирование книги
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

# Удаление книги
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'confirm_delete.html', {'book': book})







