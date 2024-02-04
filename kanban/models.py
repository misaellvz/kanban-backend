from django.db import models
from django.contrib.auth.models import User
from .choices import STATUS_CHOICES

# Create your models here.

class Kanban(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    asigned_to =  models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)