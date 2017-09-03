# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import MyIP

def index(request):
    myips = MyIP.objects.all().order_by('-created_date')
    meta = request.META
    yourip = request.META["HTTP_X_FORWARDED_FOR"]
    return render(request, 'myip/index.html', {'myips': myips, 'yourip': yourip, 'meta': request.META})

def save_myip(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = request.body
            pythonIP = request.POST.get("pythonIP", "")
            javascriptIP = request.POST.get("javascriptIP", "")
            mip = MyIP(myipaddress=javascriptIP + "/" + pythonIP)
            mip.save()
        return HttpResponse("OK")
    else:
        return HttpResponse("NOK")