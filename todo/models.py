from django.db import models
from django.contrib.auth.models import User


class Change(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def str(self):
        return self.name
