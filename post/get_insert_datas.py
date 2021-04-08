from django.core.exceptions import MultipleObjectsReturned
from .models import * 

import requests
import json
import sqlite3
import os

def get_insert_datas():
    def getName(x):

        url = "https://imdb8.p.rapidapi.com/actors/get-bio"

        querystring = {"nconst": x}

        headers = {
            'x-rapidapi-key': "709da9453fmsh5eac41924c01dd2p15fabcjsn2138cbc83099",
            'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.text)
        return (result['name'])

    url = "https://imdb8.p.rapidapi.com/actors/list-most-popular-celebs"

    querystring = {"homeCountry":"US","currentCountry":"US","purchaseCountry":"US"}

    headers = {
        'x-rapidapi-key': "709da9453fmsh5eac41924c01dd2p15fabcjsn2138cbc83099",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)
    for i in range(0,1):
        try:
            Post.objects.update_or_create(celebs_id=result[i][6:-1],name=getName(result[i][6:-1]))
        except MultipleObjectsReturned as e:
           print (e)
    posts=Post.objects.distinct()
    posts=Post.objects.values_list()
    #post=Post.objects.all().delete()
    posts=Post.objects.all()
    return posts
