from django import forms
from rucprac.models import *
class ProductForm(forms.Form):
    name_product = forms.CharField(
        max_length=100,
        label='Название продукта',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='Описание продукта'
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='Цена продукта',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )
    image = forms.ImageField(
        required=False,
        label="Цена продукта",
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['Category_Name', 'Category_Description', 'Category_FK']