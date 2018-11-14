from django.apps import AppConfig,ModelForm
from .forms import PostForm, CommentForm


class BlogConfig(AppConfig):
    name = 'Blog'

    class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
