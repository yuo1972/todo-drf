from django_filters import rest_framework as dj_filters
from .models import ToDo


class ToDoFilterSet(dj_filters.FilterSet):

    title = dj_filters.CharFilter(field_name="name", lookup_expr="icontains")
    is_active = dj_filters.CharFilter(field_name="is_done", lookup_expr="exact", exclude=True)

    order_by_field = "ordering"

    class Meta:
        model = ToDo
        fields = [
            "name",
            "is_done",
        ]
