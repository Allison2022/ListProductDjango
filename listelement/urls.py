from django.urls import path
from rest_framework import routers

from .viewsets import CategoryViewSet, TypeViewSet, ElementViewSet

route = routers.SimpleRouter()
route.register('category', CategoryViewSet)
route.register('type', TypeViewSet)
route.register('element', ElementViewSet)

urlpatterns = route.urls