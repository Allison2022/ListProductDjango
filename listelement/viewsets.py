from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Category, Type, Element
from .serializers import CategorySerializer, TypeSerializer, ElementSerializer
from django.shortcuts import get_object_or_404

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # custom methods
    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Element.objects.filter(category_id=pk)
        serializer = ElementSerializer(queryset, many=True)
        return Response(serializer.data)

    # def list(self, request):
    #     queryset = Category.objects.all()
    #     serializer = CategorySerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Category.objects.all()
    #     category = get_object_or_404(queryset, pk=pk)
    #     serializer = CategorySerializer(category)
    #     return Response(serializer.data)


class TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Type to be viewed or edited.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    # custom methods
    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Element.objects.filter(type_id=pk)
        serializer = ElementSerializer(queryset, many=True)
        return Response(serializer.data)


class ElementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Element to be viewed or edited.
    """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer