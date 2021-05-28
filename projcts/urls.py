from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectEditView,
    ProjectDeleteView,
)

urlpatterns = [
    path('', ProjectListView.as_view(), name="project_list"),
    path('<int:pk>/', ProjectDetailView.as_view(), name="project_details"),
    path('<int:pk>/edit/', ProjectEditView.as_view(), name="project_edit"),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name="project_delete"),
]