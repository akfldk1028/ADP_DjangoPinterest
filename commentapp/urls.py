from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleListView
from commentapp.views import CommentCreateView, CommentDeleteView
from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = "commentapp"

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),

]