# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import MyIP

def index(request):
    myips = MyIP.objects.all().order_by('-created_date')
    meta = request.META
    yourip = request.META["HTTP_X_FORWARDED_FOR"]
    return render(request, 'myip/index.html', {'myips': myips, 'yourip': yourip, 'meta': request.META})
    #return render(request, 'myip/index.html', {'yourip': yourip})

def save_myip(request):
    if request.is_ajax():
        if request.method == 'GET':
            print 'Raw Data: "%s"' % request.body   
    return HttpResponse("OK")