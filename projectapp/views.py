from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


# Create your views here.
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'
    # def form_valid(self, form):
    #     temp_article = form.save(commit=False)
    #     temp_article.writer = self.request.user
    #     temp_article.save()
    #     return super().form_valid(form)
    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    # form_class = CommentCreationForm
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    paginate_by = 25
    
    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None
        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                               subscription=subscription,
                                                               **kwargs)
    
#     구독정보가 있는지 없는지 확인 해야함

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 5