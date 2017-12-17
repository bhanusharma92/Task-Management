from django.db import models
from django.contrib.auth.models import User


class Label(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    date_created = models.DateField()
    last_updated = models.DateField()
    expiry = models.DateField()
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    priority = models.IntegerField()
    is_deleted = models.BooleanField(default=False)



