from django.db import models
from category.models import Category

from rest_framework import serializers

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'content', 'price', 'category']
