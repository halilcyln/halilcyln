from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import authenticate




class Category(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
    

class Todo(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateField(("Oluşturma Tarihi"),  auto_now_add=True, null=True)
    updated_at = models.DateField( ("Son Güncelleme Tarihi"), auto_now=True)
    slug = AutoSlugField(populate_from ="title" ,unique = True, null = True)

    def __str__(self):
        return self.title
class Form_page(models.Model):
    cate = models.ForeignKey(Todo, verbose_name=("Kategori seçiniz"), on_delete=models.CASCADE, null=True)
    full_name = models.CharField(("Adınızı girin"), max_length=50,null=True,blank=False)
    text = models.TextField(("Yorumunuz"),null=True)
    
    def __str__(self):
        return self.full_name
    
