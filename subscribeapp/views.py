from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


# Create your views here.

@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        # project_pk를 가지고 있는 pk 를 찾는데 없으면 404를 뱉어라  get_object_or_404
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        subscription = Subscription.objects.filter(user=user, project=project)
        # 구독정보찾는다 구독이 되어있으면 취소 아니면 구독
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super(SubscriptionView, self).get(request, *args, *kwargs)


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    def get_queryset(self):
        # values_list를 list 화시킨다
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)
        return article_list