from django.forms import ModelForm, Textarea, TextInput
from .models import Comment

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        exclude = ['post']
        widgets = {
            'author': TextInput(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'cols': 80, 'rows': 5, 'class': 'form-control'}),        }

    # post = forms.IntegerField(widget=forms.HiddenInput())
    # author = forms.CharField(label='Your name', max_length=100)
    # content = forms.CharField(widget=forms.Textarea)