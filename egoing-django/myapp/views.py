from curses.ascii import HT
import re
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
import random

topics =[
    {'id': 1, 'title': 'routing', 'body':'Routing is '},
    {'id': 2, 'title': 'mountainview', 'body': 'View is '},
    {'id': 3, 'title': 'model is park', 'body': 'Model is '},
]

def HTMLTemplate(articleTagg):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ol>
            {ol}
        </ol>
        {articleTagg}
    </body>
    </html>
    '''

def index(request):
    article = '''
    <h2>welcome</h2>
    Hello, django
    '''
    return HttpResponse(HTMLTemplate(article))

# def index(request):
#     return HttpResponse('<h1>Random</h1>'+str(random.random()))

def create(request):
    return HttpResponse('Create~')

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))