from .models import *
from .get_insert_datas import *
from django.shortcuts import HttpResponse,render
def index(request):
    
    #posts=get_insert_datas()
    return  render(request,'post/index.html',{'posts':get_insert_datas()})

