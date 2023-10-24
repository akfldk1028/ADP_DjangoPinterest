from django.forms import ModelForm

from articleapp.models import Article
from commentapp.models import Comment
from profileapp.models import Profile
from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image', 'title', 'description' ]