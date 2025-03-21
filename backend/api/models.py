from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)