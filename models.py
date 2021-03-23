from django.db import models
from django.utils import decorators,cache


class Post(models.Model):

    celebs_id = models.CharField(max_length=20, verbose_name =("ID"))
    name = models.CharField(max_length=100, verbose_name=("NAME")) # data structer

    def publish(self):
        self.celebs_id = decorators.method_decorator(self.celebs_id, name='')
        self.name = decorators.method_decorator(self.name, name='')
        self.save()
        return self.celebs_id,self.name
    

    def __str__(self):
        return self.name

