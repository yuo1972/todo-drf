from django.db import models

from datetime import datetime


class ToDo(models.Model):

    name = models.CharField(max_length=64, help_text="Список дел")
    is_done = models.BooleanField(default=False, help_text="Выполнено ли дело")
    timestamp_start = models.DateTimeField(
        auto_now_add=True, help_text="Время формирования задания"
    )
    timestamp_end = models.DateTimeField(
        blank=True, null=True, help_text="Время выполнения задания"
    )

    class Meta:
        verbose_name_plural = "Дела"

    def save(self, *args, **kwargs) -> None:
        if not self.timestamp_end and self.is_done:
            self.timestamp_end = datetime.now()
        elif self.timestamp_end and not self.is_done:
            self.timestamp_end = None
        return super().save(*args, **kwargs)
