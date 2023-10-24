from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView
from projectapp.views import ProjectCreateView, ProjectListView, ProjectDetailView
from subscribeapp.models import Subscription
from subscribeapp.views import SubscriptionView, SubscriptionListView

app_name = "subscribeapp"

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list'),

]