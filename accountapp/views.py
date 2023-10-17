from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

has_ownership = [account_ownership_required, login_required]
# Create your views here.


@login_required
def hello_world(request):
    # if request.user.is_authenticated:
        if request.method == 'POST':

            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world'))
        else:
            # 모든데이터 긁어오기
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/helloworld.html', context={'hello_world_list': hello_world_list})

    # else:
    #     return HttpResponseRedirect(reverse("accountapp:login"))

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # 계정을 만들때 성공하면 redirect하는 html
    # reverse vs reverse_lazy  차이 : 불러오는 방식의 차이가 있다. reverse를 class에서 그대로 사용이 불가하기때문에
    # reverse function // reverse_lazy : class
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

