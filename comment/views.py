from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Comment, Contact
from .forms import CommentForm, ContactForm

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
            return redirect('comment:index')
    else:
        form = CommentForm()
    return render(request, 'add.html', {'form':form})

# form view update
def update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        print(form.errors.as_text())
        if form.is_valid():
            form.save(commit=True)
            return redirect('comment:update', pk=comment.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'update.html', {'form':form, 'comment':comment})

# decorador para no exigir el tokens
from django.views.decorators.csrf import csrf_exempt

# form view Contacts
@csrf_exempt
def contact(request):
    if request.method == 'POST':
        #print(request.FILES)
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = Contact()
            contact.name = form.cleaned_data["name"]
            contact.surname = form.cleaned_data["surname"]
            contact.email = form.cleaned_data["email"]
            contact.phone = form.cleaned_data["phone"]
            contact.date_birth = form.cleaned_data["date_birth"]
            contact.sex = form.cleaned_data["sex"]
            contact.type_contact = form.cleaned_data["type_contact"]
            if "document" in request.FILES:
                contact.document = form.cleaned_data["document"]
            contact.save()
            #print("valido: "+ str(form.cleaned_data["typeContact"].id))
            messages.add_message(request, messages.SUCCESS, "Contacto creado con exito")
            return redirect("comment:contact")
        else:
            return "data invalid"
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})