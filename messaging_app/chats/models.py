"""Django app models."""
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Represents a user that extends from the Abstract user in the Django app."""
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    ROLE_CHOICES = [
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')
    created_at = models.DateTimeField(auto_now_add=True)


class Conversation(models.Model):
    """Represents a conversation in the Django app."""
    conversation_id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(User, related_name='conversations')


class Message(models.Model):
    """Represents a message in the Django app."""
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
