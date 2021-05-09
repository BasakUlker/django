from django.shortcuts import render, get_object_or_404,HttpResponse,HttpResponseRedirect, redirect
from django.db import connections
from .models import *
from .tvShowsAndFilms import *
from .forms import Post2Form
from django.contrib import messages
import json
from django.http import QueryDict

def post2_index(request):
    
    posts=Post2.objects.all()
    
    if request.method == 'POST':
        response = json.dumps(dict(request.POST.lists()))
        result = json.loads(response)
        context={
                'posts':",".join(result['shows']),
        }
        return render(request,'post2/choises.html',context) 
    
    context = {
        'posts':posts,
    }
    return render(request,'post2/post2_index.html',context)

def home(request):

    return render(request, "post2/home.html")


