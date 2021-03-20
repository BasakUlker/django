from django.shortcuts import render
from django.shortcuts import HttpResponse 
import requests
import json
import sqlite3
import os

# Create your views here.
#index is the view.
def index(request):

    #insertName function is my part of app. this def returns a database that include api datas below.
    def insertName(name):

        with sqlite3.connect('celebsname.sqlite') as celebsname:

            im=celebsname.cursor()

            im.execute("""CREATE TABLE IF NOT EXISTS celebsname (Name)""")


            if os.path.exists("celebsname.sqlite"):
                im.execute("""INSERT INTO celebsname VALUES (?)""",[name])
                celebsname.commit()
            im.close()
            return celebsname
    #this def returns 'name' information of parameter from "https://imdb8.p.rapidapi.com/actors/get-bio".
    def getName(x):

        url = "https://imdb8.p.rapidapi.com/actors/get-bio"

        querystring = {"nconst": x}

        headers = {
            'x-rapidapi-key': " ",#Before you try, you have to get a key from RapidApi.
            'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.text)#listed "response.text" for index process
        return (result['name'])

    #this part is for getting id datas from the api in below.( "https://imdb8.p.rapidapi.com/actors/list-most-popular-celebs")
    url = "https://imdb8.p.rapidapi.com/actors/list-most-popular-celebs"

    querystring = {"homeCountry":"US","currentCountry":"US","purchaseCountry":"US"}

    headers = {
        'x-rapidapi-key': " ",#Before you try, you have to get a key from RapidApi. 
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)
    for i in range(0,10):#id's are sent "getName()"function one by one and added on database with "insertName"function.
        name = getName(result[i][6:-1])
        #print(name)
        insertName(name)

    im = insertName(None).cursor()
    im.execute("SELECT * FROM celebsname")
    al = im.fetchall()#selected all of datas from "celebsname" db


    return HttpResponse("{}".format(al))#published datas on homepage
