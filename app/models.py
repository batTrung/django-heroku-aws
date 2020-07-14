from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="users/")

    def __str__(self):
        return self.name
