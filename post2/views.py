from django.shortcuts import render, get_object_or_404,HttpResponse,HttpResponseRedirect, redirect
from django.db import connections
from .models import *
from .tvShowsAndFilms import *
from .forms import Post2Form
from django.contrib import messages
import json
from django.http import QueryDict
from django.urls import NoReverseMatch
from django.core.exceptions import MultipleObjectsReturned
from django.utils.datastructures import MultiValueDictKeyError
def post2_index(request):
    
    posts=Post2.objects.all()
    filmdatas=films.objects.all()
    seriesdatas=movieseries.objects.all()
    if request.method == 'POST':
        response = json.dumps(dict(request.POST.lists()))
        result = json.loads(response)
        datas = usersdata.objects.all().delete()
        my_list = request.POST.getlist("shows")
        my_list2 = request.POST.getlist("data")
        my_list3 = request.POST.getlist("data2")
        for i in range(len(my_list)):
            try:
                datas = usersdata.objects.update_or_create(datas=my_list[i]) 
            except MultipleObjectsReturned as e:
                pass
            except MultiValueDictKeyError: 
                pass
        for i in range(len(my_list2)):
            try:
                datas = usersdata.objects.update_or_create(datas=my_list2[i]) 
            except MultipleObjectsReturned as e:
                pass
            except MultiValueDictKeyError: 
                pass
        for i in range(len(my_list3)):
            try:
                datas = usersdata.objects.update_or_create(datas=my_list3[i]) 
            except MultipleObjectsReturned as e:
                pass
            except MultiValueDictKeyError: 
                pass

        datas = usersdata.objects.distinct()
        datas = usersdata.objects.values_list()
        return redirect("yourlist")
    context = {
        'posts':posts,
        'filmdatas':filmdatas,
        'seriesdatas':seriesdatas,
    }
    return render(request,'post2/post2_index.html',context)

def yourlist(request):

    datas = usersdata.objects.all()
    context={
            'posts':datas,
            }
    return render(request,'post2/choises.html',context)
def editpage(request):
    datas = usersdata.objects.all()
    if request.method=='POST':
        response = json.dumps(dict(request.POST.lists()))
        result = json.loads(response)
        context={
            'posts':",".join(result['shows']).split(","),
        }
        datas = usersdata.objects.all().delete()
        for i in range(len(result["shows"])):
            datas = usersdata.objects.create(datas=result["shows"][i])
        datas = usersdata.objects.distinct()
        datas = usersdata.objects.values_list()

        return render(request,'post2/choises.html',context)
    context={
            'posts':datas,
            }
    return render(request,'post2/editpage.html',context)

def home(request):

    return render(request, "post2/home.html")


