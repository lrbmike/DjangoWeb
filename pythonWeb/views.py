# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.shortcuts import render
from django.http import HttpResponse
import datetime

from django.db import connection

from django.shortcuts import render_to_response

# Create your views here.

def current_datetime(request):
    now = datetime.datetime.now()

    # html = "<html><body>It is now %s.</body></html>" % now

    templateHtml = 'time_now.html'
    data = {'now': str(now)}

    return render_to_response(templateHtml, data)


def hours_ahead(request, offset):
    offset = int(offset)
    print ("offset: " + str(offset))
    now = datetime.datetime.now()

    print "now: " + str(now)
    dt = now + datetime.timedelta(days=offset)
    print ("time: " + str(dt))
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def show_list(request):

    cur = connection.cursor()
    cur.execute('select * from test1')

    html = "";

    for row in cur.fetchall():
        html += str(row[0]) + '<|>' + str(row[1]);


    cur.close()
    connection.close()

    return HttpResponse(html)

from pythonWeb import models

def insert_user(request):

    p1 = models.User(name='刘一', age=12, createTime=datetime.datetime.now())
    p1.save()

    html = "<html><body>It is now %s.</body></html>" % 'insert success!'

    return HttpResponse(html)

#查询user表所有的用户
def show_user(request):

    # html = "";
    #
    # for user in models.User.objects.all():
    #     html += user.__str__()

    object_list = models.User.objects.all()
    template_html = 'user_list.html';
    data = {'object_list': object_list}

    return render_to_response(template_html,data)

#根据用户名查询用户
def show_user_name(request, userName):

    html = "";

    keyName = str(userName)

    for user in models.User.objects.filter(name = keyName):
        html += user.__str__()

    return HttpResponse(html)


from django_websocket import require_websocket

@require_websocket
def echo_once(request):
    message = request.websocket.wait()
    print message
    message += 'hello '
    request.websocket.send(message)





