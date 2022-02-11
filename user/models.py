from mailbox import NotEmptyError
from django.db import models


class UserProfile(models.Model):
    """Model para armazenar dados básicos dos usuários"""

    name = models.CharField(max_length=255) 
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
