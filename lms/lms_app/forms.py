from django import forms
from matplotlib import widgets
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']
        widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),

        }


class BookForm(forms.ModelForm):
        class Meta:
            model = Book
            fields = [
                'title',
                'auther',
                'photo_book',
                'photo_auther',
                'pages',
                'prices',
                'retal_price_day',
                'retal_period',
                'status',
                'category',               
            ]
            
            widgets = {
                'title':forms.TextInput(attrs={'class':'form-control'}),
                'auther':forms.TextInput(attrs={'class':'form-control'}),
                'photo_book':forms.FileInput(attrs={'class':'form-control'}),
                'photo_auther':forms.FileInput(attrs={'class':'form-control'}),
                'pages':forms.NumberInput(attrs={'class':'form-control'}),
                'prices':forms.NumberInput(attrs={'class':'form-control'}),
                'retal_price_day':forms.NumberInput(attrs={'class':'form-control'}),
                'retal_period':forms.NumberInput(attrs={'class':'form-control'}),
                'status':forms.Select(attrs={'class':'form-control'}),
                'category':forms.Select(attrs={'class':'form-control'}),

                

                
            }
