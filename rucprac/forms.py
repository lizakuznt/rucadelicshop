from django import forms
from rucprac.models import Product, Category  # Явный импорт моделей

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Product_Name', 'Product_Description', 'Product_Price', 'Product_Picture']  # Параметры модели для формы
        widgets = {
            'Product_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Product_Description': forms.Textarea(attrs={'class': 'form-control'}),
            'Product_Price': forms.NumberInput(attrs={'class': 'form-control'}),
            'Product_Picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['Category_Name', 'Category_Description', 'Category_FK']
        widgets = {
            'Category_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Category_Description': forms.Textarea(attrs={'class': 'form-control'}),
            'Category_FK': forms.Select(attrs={'class': 'form-control'}),
        }
