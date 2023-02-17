from django.shortcuts import render
from .models import Comment

# index view
def index(request):
    comments = Comment.objects.all()
    response = {
        'comments':comments
    }
    return render(request, 'index.html', response)