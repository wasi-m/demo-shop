from django.db import models

from rest_framework import serializers

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return 'Category: {}'.format(self.name)

class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='subcategories'
    )
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'subcategories')

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['subcategories'] = CategorySerializer(many=True)
        return fields

    def create(self, validated_data):
        del validated_data['subcategories']
        obj = Category.objects.create(**validated_data)
        obj.save()
        return obj

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.parent = validated_data['parent']
        instance.save()
        return instance
