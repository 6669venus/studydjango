# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

@csrf_protect
def signup(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = request.body
            signup_email = request.POST.get("signup_email", "")
            signup_password = request.POST.get("signup_password", "")
            user = User.objects.create_user(signup_email, signup_email, signup_password)
        return JsonResponse({'result':'success'})
    else:
        return JsonResponse({'result':'error'})

@csrf_protect        
def login(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = request.body
            signup_email = request.POST.get("signup_email", "")
            signup_password = request.POST.get("signup_password", "")
            user = User.objects.create_user(signup_email, signup_email, signup_password)
        return JsonResponse({'result':'success'})
    else:
        return JsonResponse({'result':'error'})