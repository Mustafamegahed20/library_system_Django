from unicodedata import category
from django.db import models
from matplotlib.pyplot import title
from matplotlib.style import available

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    
    status_book=[
        ('available','available'),
        ('retal','retal'),
        ('sold','sold'),
    ]
    
    title=models.CharField(max_length=250)
    auther=models.CharField(max_length=250,null=True,blank=True)
    photo_book=models.ImageField(upload_to='photos',null=True,blank=True)
    photo_auther=models.ImageField(upload_to='photos',null=True,blank=True)
    pages=models.IntegerField(null=True,blank=True)
    prices=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    retal_price_day=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    retal_period=models.IntegerField(null=True,blank=True)
    total_rental=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    active=models.BooleanField(default=True)
    status=models.CharField(max_length=250,choices=status_book,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.title