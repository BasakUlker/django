from django.shortcuts import render, HttpResponse,HttpResponseRedirect, redirect
from django.db import connections
from .models import *
from .tvShowsAndFilms import *
from .forms import Post2Form
from django.contrib import messages

def post2_index(request):

    posts=Post2.objects.all()

    context = {
        'posts':posts,
    }
    return render(request,'post2/form.html',context)


