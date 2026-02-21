"""
Database models for chats-related tables.

Includes:
- User: Custom user model extending Django's AbstractUser.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    """
    Represents a user in the application.

    Extends from Django's AbstractUser with custom fields.

    Attributes:
        id (UUID): Primary key identifier for the user (indexed).
        first_name (str): User's first name (required).
        last_name (str): User's last name (required).
        email (str): Unique email address used for authentication.
        phone_number (str | None): Contact phone number.
        role (str): User role in the system (guest, host, or admin).
        created_at (datetime): Timestamp of user creation (auto-generated).
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    role_choices = [
        ("guest", "Guest"),
        ("host", "Host"),
        ("admin", "Admin"),
    ]
    role = models.CharField(max_length=10, choices=role_choices)
    created_at = models.DateTimeField(auto_now_add=True)
