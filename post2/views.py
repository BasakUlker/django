from django.shortcuts import render, HttpResponse
from django.db import connections
from .models import *
from .tvShowsAndFilms import *

def post2_index(request):

    return render(request,'post2/post2_index.html',{'posts':tvShowsNFilms()})
