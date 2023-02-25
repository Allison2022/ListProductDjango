from django.forms import ModelForm, Textarea
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text':Textarea(attrs={'class':'form-input'})
        }

        '''def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['text'].widget.attrs.update({'class':'form-input'})'''
        
        def save(self,commit=True, text=""):
            instance = super(CommentForm, self).save(commit=commit)

            if(text == ""):
                instance.text = text #"No podras modificarme"

            if (commit):
                instance.save()

# building form with django form api
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=10, min_length=2)
    
    # name = forms.CharField(label='Nombre', validators=[MinLengthValidator(2,message="Ensure this value has at least %(limit_value)d characters (it has "
    #     "%(show_value)d)."), MaxLengthValidator(15,message="Ensure this value has at most %(limit_value)d character (it has "
    #     "%(show_value)d).")])# clase para hacer validaciones
    
    surname = forms.CharField(label='Apellido', required=False, max_length=10, min_length=2)
    
    phone = forms.RegexField(label='Telefono', regex="^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$", max_length=13, min_length=10)
    
    email = forms.EmailField('Email') #esto es a modo de prueba solamente forms.CharField(label='Email', validators=[EmailValidator(message="Invalid email", allowlist=["gmail"])])
    
    date_birth = forms.DateField(label='Fecha de nacimiento')







