from rest_framework import viewsets, mixins
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from .filters import ToDoFilterSet
from rest_framework.schemas.openapi import AutoSchema

from .models import ToDo
from .serializers import ToDoSerializer


class FullListView(ListView):
    context_object_name = "todo_"
    queryset = ToDo.objects.all()
    template_name = "todo_list.html"


class FullListViewOn(ListView):
    context_object_name = "todo_"
    queryset = ToDo.objects.filter(is_done=True)
    template_name = "todo_list_on.html"


class FullListViewOff(ListView):
    context_object_name = "todo_"
    queryset = ToDo.objects.filter(is_done=False)
    template_name = "todo_list_off.html"


class ToDoCreateView(CreateView):
    model = ToDo
    fields = ["name", "is_done"]
    template_name = "todo_create.html"
    success_url = "/list/"


class ToDoDeleteView(DeleteView):
    model = ToDo
    template_name = "todo_delete.html"
    success_url = reverse_lazy("load")


class ToDoUpdateView(UpdateView):
    model = ToDo
    fields = ["name", "is_done"]
    template_name = "todo_edit.html"
    success_url = reverse_lazy("load")


class ToDoViewSet(
    mixins.ListModelMixin,  # GET /tasks
    mixins.CreateModelMixin,  # POST /tasks
    mixins.RetrieveModelMixin,  # GET /articles/1
    mixins.DestroyModelMixin,  # DELETE /articles/1
    mixins.UpdateModelMixin,  # PUT /articles/1
    viewsets.GenericViewSet
):

    queryset = ToDo.objects.all().order_by("-id")
    serializer_class = ToDoSerializer
    filterset_class = ToDoFilterSet

    schema = AutoSchema(
        tags=['ToDoList'],
        component_name='ToDo',
        operation_id_base='ToDo',
    )
