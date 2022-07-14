from curses.ascii import HT
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
# import random
from django.views.decorators.csrf import csrf_exempt

nextId = 4
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
        <ul>
        <li><a href="/create/">create</a></li>
        </ul>
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


def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="입력하세요^^"></p>
            <p><textarea name="body" placeholder="이것도 입력하세요~"></textarea><p>
            <p><input type="submit"></p>
            </form>
    '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextId, "title":title, "body":body}
        topics.append(newTopic)
        url = '/read/'+str(nextId)
        nextId = nextId + 1
        return redirect(url)
