from django.db import models
from django.utils import decorators,cache

class Post(models.Model):

    celebs_id = models.CharField(max_length=20, verbose_name =("ID"))
    name = models.CharField(max_length=100, verbose_name=("NAME"))


    def __str__(self):
        return self.name

