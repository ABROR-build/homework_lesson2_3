from django.db import models
from django.contrib.auth.models import AbstractUser


class Candidates(AbstractUser):
    age = models.IntegerField(default=19)