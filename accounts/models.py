from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Account(AbstractUser):
    class Role(models.TextChoices):
        MANAGER = 'MANAGER', 'Manager'
        AGENT = 'AGENT', 'Agent'
        CUSTOMER = 'CUSTOMER', 'Customer'

    base_role = Role.MANAGER
    role = models.CharField(max_length=50, choices=Role.choices)

    REQUIRED_FIELDS = ['role']

