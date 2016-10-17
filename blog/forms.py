from django.forms import ModelForm, Textarea, TextInput
from haystack.forms import SearchForm
from .models import Comment

# Form to include comments to a post
class CommentForm(ModelForm):

    class Meta:
        model = Comment
        # post field excluded of the form and handled on the view
        exclude = ['post']
        widgets = {
            'author': TextInput(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'cols': 80, 'rows': 5, 'class': 'form-control'}),
        }