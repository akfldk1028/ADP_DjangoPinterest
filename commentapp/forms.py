from django.forms import ModelForm

from articleapp.models import Article
from commentapp.models import Comment
from profileapp.models import Profile


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']