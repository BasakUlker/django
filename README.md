# django

Here is my firts project with django. 

# Requirements
- SQLite3
- Signing Up to RapidApi for Api Keys in the program:
  * https://rapidapi.com/apidojo/api/imdb8/endpoints
    - Endpoints:
    - get-bio
    - list-most-popular-celebs
    - get-plots
    - get-top-rated-tv-shows
    - get-most-popular-movies
    - get-coming-soon-tv-shows
- Boostrap CSS
- render, get_object_or_404, HttpResponseRedirect, redirect, HttpResponse Modules from django.shortcuts
- MultipleObjectsReturned module from django.core.exceptions
- json Module
- os Module
- from django.http import QueryDict
- from django.urls import NoReverseMatch
- `pip install requests`
- `pip install pysqlite3`

# Program

It's a view page that based on django framework.
Home Page:
![](https://github.com/BasakUlker/django/blob/main/Screenshot%20from%202021-06-02%2019-35-30.png)
Form Page:
![](https://github.com/BasakUlker/django/blob/main/Screenshot%20from%202021-06-02%2019-35-41.png)
Chosen Datas from Form Page:
![](https://github.com/BasakUlker/django/blob/main/Screenshot%20from%202021-06-02%2019-35-55.png)
Edit Page
![](https://github.com/BasakUlker/django/blob/main/Screenshot%20from%202021-06-02%2019-36-02.png)


# Explanation

Datas, where getting from IMDb api, are registered in a database. After this part, datas are selected and shown on a html page in this program. Boostrap CSS was integrated for style.
