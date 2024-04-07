from django.forms import ModelForm
from books.models import Book
from django import forms


class BooksForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['title', 'author', 'price', 'publication_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'number_of_pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
