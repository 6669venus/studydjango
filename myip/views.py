# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import MyIP

def index(request):
    myips = MyIP.objects.all().order_by('-created_date')
    yourip = "111.222.333.111/233.535.66.77"
    return render(request, 'myip/index.html', {'myips': myips, 'yourip': yourip})
    #return render(request, 'myip/index.html', {'yourip': yourip})
    