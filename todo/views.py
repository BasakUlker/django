from django.shortcuts import render
from django.shortcuts import HttpResponse 
import requests
import json
import sqlite3
import os

# Create your views here.

def index(request):

    def insertName(name):

        with sqlite3.connect('celebsname.sqlite') as celebsname:

            im=celebsname.cursor()

            im.execute("""CREATE TABLE IF NOT EXISTS celebsname (Name)""")


            if os.path.exists("celebsname.sqlite"):
                im.execute("""INSERT INTO celebsname VALUES (?)""",[name])
                celebsname.commit()
            im.close()
            return celebsname

    def getName(x):

        url = "https://imdb8.p.rapidapi.com/actors/get-bio"

        querystring = {"nconst": x}

        headers = {
            'x-rapidapi-key': "3ee414594bmsh95d08663d649adap12c8cbjsnf6e902276553",
            'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.text)
        return (result['name'])


    url = "https://imdb8.p.rapidapi.com/actors/list-most-popular-celebs"

    querystring = {"homeCountry":"US","currentCountry":"US","purchaseCountry":"US"}

    headers = {
        'x-rapidapi-key': "3ee414594bmsh95d08663d649adap12c8cbjsnf6e902276553",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)
    for i in range(0,10):
        name = getName(result[i][6:-1])
        #print(name)
        insertName(name)

    im = insertName(None).cursor()
    im.execute("SELECT * FROM celebsname")
    al = im.fetchall()



    return HttpResponse("{}".format(al))
