from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


