from django.forms import ModelForm, Textarea
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
            self.fields['text'].widget.attrs.update({'class':'form-input'})        '''