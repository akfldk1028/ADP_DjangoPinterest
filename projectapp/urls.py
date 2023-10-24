from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView
from projectapp.views import ProjectCreateView, ProjectListView, ProjectDetailView

app_name = "projectapp"

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    # path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
    path('list/', ProjectListView.as_view(), name='list'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),

]