from .models import *
from .get_insert_datas import *
from django.shortcuts import HttpResponse,render
from django.db import connections

def index(request):
    

    return  render(request,'post/index.html',{'posts':get_insert_datas()})

