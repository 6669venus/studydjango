# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from myip.models import MyIP

def index(request):
    return render(request, 'website/index.html', {})
    
# def login(request):
#     if request.is_ajax():
#         if request.method == 'POST':
#             data = request.body
#             pythonIP = request.POST.get("pythonIP", "")
#             javascriptIP = request.POST.get("javascriptIP", "")
#             mip = MyIP(myipaddress=javascriptIP + "/" + pythonIP)
#             mip.save()
#         return HttpResponse("OK")
#     else:
#         return HttpResponse("NOK")
        
def signup(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = request.body
            signup_email = request.POST.get("signup_email", "")
            signup_password = request.POST.get("signup_password", "")
            mip = MyIP(myipaddress=signup_email + "/" + signup_password)
            mip.save()
        return HttpResponse("OK")
    else:
        return HttpResponse("NOK")