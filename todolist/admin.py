from django.contrib import admin
from .models import ToDo


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "is_done",
        "timestamp_start",
        "timestamp_end",
    )
    readonly_fields = ["timestamp_start", "timestamp_end"]
    list_filter = ["is_done"]
    search_fields = ("name",)
