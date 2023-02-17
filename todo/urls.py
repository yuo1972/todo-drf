from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

from todolist.views import (
    FullListView,
    FullListViewOn,
    FullListViewOff,
    ToDoCreateView,
    ToDoDeleteView,
    ToDoUpdateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', FullListView.as_view(), name='load'),
    path('list/on/', FullListViewOn.as_view(), name='load_on'),
    path('list/off/', FullListViewOff.as_view(), name='load_off'),
    path('add/', ToDoCreateView.as_view(), name='add'),
    path('delete/<int:pk>/', ToDoDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', ToDoUpdateView.as_view(), name='edit'),
    path("api/", include("todolist.urls")),

    path('openapi/', get_schema_view(
        title="Studying",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),

]
