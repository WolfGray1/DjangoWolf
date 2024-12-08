from django import forms
from .models import Book

class UploadImageForm(forms.Form):
    image = forms.ImageField()
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Ваше имя")
    email = forms.EmailField(required=True, label="Ваш email")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Сообщение")
class UserForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    age = forms.IntegerField(label="Возраст", min_value=0, max_value=120, required=True)
    def clean_name(self):
        name = self.cleaned_data['name']
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Имя не должно содержать чисел.")
        return name
class BookForm(forms.ModelForm):
    published_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})  # HTML5-виджет для выбора даты
    )
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'description', 'price']











