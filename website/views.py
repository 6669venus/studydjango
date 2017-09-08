# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from myip.models import MyIP
from django.contrib.auth.models import User

def index(request):
    return render(request, 'website/index.html', {})
    
