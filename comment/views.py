from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import CommentForm

# index view
def index(request):
    comments = Comment.objects.all()
    response = {
        'comments':comments
    }
    return render(request, 'index.html', response)

# form view
def add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
    else:
        form = CommentForm()
    return render(request, 'add.html', {'form':form})

# form view update
def update(request, pk):

    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('update', pk=comment.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'update.html', {'form':form, 'comment':comment})