from django.db import models
from django.utils import decorators,cache

class Post2(models.Model):

    shows = models.CharField(max_length=100, verbose_name =("Top Rated Tv Shows"))

    def __str__(self):
        return self.shows

