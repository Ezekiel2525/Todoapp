#REST API (Application Programming Interface)
"""
Django REST Framework is a framework developed for the purpose of 
letting your website applications interact with other developers or
websites.

An API refers to a set of protocols and tools that allow interaction 
between two different applications. 
In simple terms, it is a technique that enables 
third-party vendors to write programs that can easily interface with each other. 
Before we proceed, let's do few things here,
let's learn how to install files from requirements files

create a new file and name it requirements.txt, and list all softwares you want to install for your project
go to your project and pip install requirements.txt
consider installing softwares like django, django-crispy-forms, Pillow, django-rest-framework, crispy-bootstrap
all these can be listed in the requirements.txt file.

Building your first api
Let's create a venv and start a project in side it


Let's start a project and call it any name using django
we can create a new folder and call it pyclient
Let's create a file and call it basic.py

WHAT IS AN ENDPOINT?
An endpoint is the place of interaction between applications. 
API refers to the whole set of protocols that allows communication 
between two systems while an endpoint is a URL that enables the 
API to gain access to resources on a server.
Consider the endpoint as the url of the server that you are going to e.g. github.com

working with api
https://httpbin.org/status/200
https://httpbin.org/anything
we need to import requests

consider a situation whereby we want to get the endpoint of github.com, we can specify our endpoint
to be github.com
import requests
endpoint = 'https://httpbin.org'
endpoint = 'https://httpbin.org/anything' #What this will do is to allow us get anything from the server

get_response = requests.get(endpoint)
let's pring get_response
print(get_response.text)

a regular http request will return html
while a API HTTP request will return xml or json
WHAT IS JSON?
Javascript Objects Notation is what Json stants for, it is very related to python dictionary

i can convert the json to a python dictionary
print(get_response.json())

We need to learn about status codes
print(get_response.status_code)
this will bring 200 if the protocol runs successfully
404 shows page not found
we can check it out on httpbin.org/status


Let's now start a basic django project and runserver
we are supposed to have it running using https://127.0.0.1:8080
let's now turn this to our endpoint
endpoint = 'http://127.0.0.1:8080'
now, we have been able to create our first API
Let's create our first API View

let's create our views

in our app views, let's import JsonResponse
from django.http import JsonResponse

def api_view(request):
    return JsonResponse({'status': 'This is a successful message'})

we can show our views in url and then display it

To confirm our api, we can go and run the basic.py app

let's make it more spicy
get_response = requests.get(endpoint, json={'message': 'This is to make it more spicy'})

print(get_response.json())

in our app views, we can import json to convert our response to a dictionary readable content

import json
from django.http import JsonResponse

def api_view(request):
    body = json.loads(request.body)
    data = {}
    try:
        data=json.loads(body)
    except:
        prrint('error parsing json')
    
        
    we can add the content type to the data
    data['content_type'] = request.content_type
    # print(data['message'])
    print(data)

    return JsonResponse(data)

Django Models Instance as An Api Response
Let's echo back what is in our database to our api

Let's create a simple model
class MyModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True, null=True)
    price = models.FloatFied(decimal_places=2, max_digits=10, default= 10.00)

We need to migrate, after migration, then let's import the model and then grab the objects
def api_view(request):
    model_data =MyModel.objects.order_by(id)
    data ={}
    if model_data:
        data['title'] = model_data.title
        data['text'] = model_data.text
        data['price'] = model_data.price
    
        
    return JsonResponse(data)

if we print our basic.py, we should be to see our results in dictionary

Django Model Instance to Dictionary
To turn a django model into a dictionary,
we neet to import model_to_dict

from django.forms.model import model_to_dict

ef api_view(request):
    model_data =MyModel.objects.order_by(id)
    data ={}
    if model_data:
        data = model_to_dict(model_data)
        we can also specity the fields we want to add in
        data = model_to_dict(model_data, fields=['title', 'price'])
    
        
    return JsonResponse(data)

"""