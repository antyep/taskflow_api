from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Role(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('mod', 'Moderator'),
        ('user', 'User'),
    ]

    name = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.name


class CustomUser(User):
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True)


def __str__(self):
    return self.username


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]

    title = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class TaskTag(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
