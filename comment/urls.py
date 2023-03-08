from django.urls import path
from . import views

app_name = 'comment'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('update/<int:pk>', views.update, name='update'),
    path('contact', views.contact, name='contact'),
]