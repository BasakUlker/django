from .models import *
from .get_insert_datas import *
from django.shortcuts import HttpResponse
def index(request):

    return HttpResponse(get_insert_datas()) 

