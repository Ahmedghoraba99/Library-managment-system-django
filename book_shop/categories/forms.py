from django.forms import ModelForm
from categories.models import Category
from django import forms


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-3', 'rows': 3}),

        }
