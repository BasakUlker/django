from django.core.exceptions import MultipleObjectsReturned
from .models import *

import requests
import json
import sqlite3
import os

def get_insert_datas():
    
    #this def returns 'name' information of parameter from "https://imdb8.p.rapidapi.com/actors/get-bio".
    def getName(x):

        url = "https://imdb8.p.rapidapi.com/actors/get-bio"

        querystring = {"nconst": x}

        headers = {
            'x-rapidapi-key': " ", #Before you try, you have to get a key from RapidApi.
            'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.text) #listed "response.text" for index process

        return (result['name'])
    
    #this part is for getting id datas from the api in below.( "https://imdb8.p.rapidapi.com/actors/list-most-popular-celebs")
    url = "https://imdb8.p.rapidapi.com/actors/list-most-popular-celebs"

    querystring = {"homeCountry":"US","currentCountry":"US","purchaseCountry":"US"}

    headers = {
        'x-rapidapi-key': " ", #Before you try, you have to get a key from RapidApi.
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)
    for i in range(0,5): #id's are sent "getName()"function one by one and added on the database.
        try:
            Post.objects.update_or_create(celebs_id=result[i][8:-1],name=getName(result[i][6:-1])) #create database object 
        except MultipleObjectsReturned as e:
            print (e)
    posts=Post.objects.distinct() #distinct same datas
    posts=Post.objects.values_list() #listing datas

    return posts
