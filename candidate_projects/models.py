from django.db import models
from django.contrib.auth import get_user_model


class Projects(models.Model):
    project_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    project_details = models.TextField()
