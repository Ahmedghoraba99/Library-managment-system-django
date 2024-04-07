from django import forms
from django.forms import ModelForm
from categories.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()

        for field_name, field_value in cleaned_data.items():
            if not field_value:
                raise forms.ValidationError(
                    f"{field_name.capitalize()} is required.")

        return cleaned_data
