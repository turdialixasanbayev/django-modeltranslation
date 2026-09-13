from django.db import models


class Todo(models.Model):
    title         = models.CharField(max_length=200)
    description   = models.TextField(blank=True, null=True)
    completed     = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {'Completed' if self.completed else 'Not Completed'}"
