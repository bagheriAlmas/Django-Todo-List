from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class TodoList(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists')

    # def get_absolute_url(self):
    #     return reverse('model_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class TodoItem(models.Model):
    PRIORITY_ITEMS = (
        ("low", "Low"),
        ("normal", "Normal"),
        ("high", "High")
    )

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    finished = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_ITEMS, default='low')
    status = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='items')

    class Meta:
        ordering = ['-created', ]

    def __str__(self):
        return f"{self.title} - {self.todo_list}"
