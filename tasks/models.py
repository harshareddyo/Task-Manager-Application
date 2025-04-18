# tasks/models.py

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    # ✅ Add this line:
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

