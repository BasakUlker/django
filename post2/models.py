from django.db import models
from django.urls import reverse

class Post2(models.Model):

    shows = models.CharField(max_length=100, verbose_name =("tv shows"))

    def __str__(self):
        return self.shows
    def get_absolute_url(self):
        return reverse('yourlist', kwargs={'context':self.context})

class films(models.Model):
    film = models.CharField(max_length=100, verbose_name =("films"))
    def __str__(self):
        return self.film
class movieseries(models.Model):
    series = models.CharField(max_length=100, verbose_name =("movie series"))
    def __str__(self):
        return self.series

class usersdata(models.Model):

    datas = models.CharField(max_length=100, verbose_name =("choises"))
    def __str__(self):
        return self.datas

