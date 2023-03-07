from rest_framework import serializers
from listelement.models import Category, Type, Element

# class serializer Category model.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# class serializer Type model.
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

# class serializer Element model.
class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = '__all__'