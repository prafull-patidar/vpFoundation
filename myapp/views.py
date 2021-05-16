from django import template
from django.core.mail.message import EmailMultiAlternatives
from django.shortcuts import render,redirect,get_object_or_404
# from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.core.mail import EmailMessage
from django.contrib.auth import login,authenticate,logout
from django.views import View
from django.urls import reverse
import re
# from useraccount.forms import CustomPasswordResetForm
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
# from .utils import token_generator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
import datetime
from django.utils import timezone
from datetime import timedelta
import json
from django.views.decorators.csrf import csrf_exempt
import random

from django.template import Context
from django.template.loader import render_to_string,get_template
from django.core.mail import EmailMessage
from smtplib import SMTPException
from django.conf import settings

# import models
from myapp.models import joinUsModel,helpModel,Contact

import os
# from twilio.rest import Client

def home(request):
    return render(request,"home.html")

def joinform(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        wpphone = request.POST.get('wpphone')
        address = request.POST.get('address')
        occupation = request.POST.get('occupation')
        message = request.POST.get('message','')
        otp = random.randint(1000,9999)

        try:
            user_data = joinUsModel.objects.get(email=email)
            if user_data is not None and user_data.varified:
                return JsonResponse({'Error':"You are Already Joined with us"})
            else:
                user_data = joinUsModel(name=name,email=email,phone=phone,wpPhone=wpphone,address=address,occupation=occupation,message=message)
                user_data.save()
                request.session['username']=name
                request.session['userIdentity']= email
                request.session['varified'] = False
                email_subject = "Ved Prakash Foundation"
                template_name = "mail.html"
                ctx = {
                    'username': name,
                    'otp':otp
                }
                email_status = sendMail(email_subject,email,template_name,ctx)
                data = {}
                if(email_status == 'success'):
                    data['myOtp'] =encotp(otp)
                elif(email_status == 'error'):
                    data['myOtp'] = 'none'
                return JsonResponse(data,status=200)

        except joinUsModel.DoesNotExist:
            user_data = joinUsModel(name=name,email=email,phone=phone,wpPhone=wpphone,address=address,occupation=occupation,message=message)
            user_data.save()
            request.session['username']=name
            request.session['userIdentity']= email
            request.session['varified'] = False
            
            email_subject = "Ved Prakash Foundation"
            template_name = "mail.html"
            ctx = {
                    'username': name,
                    'otp':otp
            }
            email_status = sendMail(email_subject,email,template_name,ctx)
            data = {}
            if(email_status == 'success'):
                data['myOtp'] =encotp(otp)
            elif(email_status == 'error'):
                data['myOtp'] = 'none'
            return JsonResponse(data,status=200)
    return redirect('home')

def validateUser(request):
    if request.method == "POST":
        otp = request.POST.get('otp')
        user_email = request.session.get('userIdentity')
        user  = joinUsModel.objects.filter(email=user_email)
        user.update(varified=True)
        request.session['varified'] = True
        data = {}
        data['varified']=True
        return JsonResponse(data,status=200)
    return redirect('home')

# function to encode otp
def encotp(otp):
    otp = int(otp)
    dummyotp = otp*50/20
    return dummyotp

# function to send email to user
def sendMail(subject,mail,template_name,ctx):
    print(template_name)
    message = get_template(template_name).render(ctx)
    try:
        msg = EmailMessage(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [mail],
        )
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
        print('success email')
        return "success"
    except SMTPException as e:
        print(e)
        return "error"

# help form view
def needhelp(request):
    if request.method == 'POST':
        help_str = request.GET.get('type','')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        wpphone = request.POST.get('wpphone', '')
        currentAdd = request.POST.get('currentAdd')
        permanentAdd = request.POST.get('permanentAdd', '')
        message = request.POST.get('message','')
        city = request.POST.get('city')
        help_type = help_str
        helpModel(name=name,email=email,phone=phone,wpPhone=wpphone,currentAddress=currentAdd,permanentAddress=permanentAdd,city=city,message=message,help_type=help_type).save()

        data = {
            'req_status':'success'
        }
        return JsonResponse(data,status=200)
    help_str = request.GET.get('type','')
    return render(request,'needhelp.html',{'help_type':help_str})

# contact form data submit

def contact(request):
    if request.method == "POST":
        suggestion = request.POST.get('suggestion')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        print(suggestion)
        print(name)
        print(email)
        print(subject)
        Contact(suggestion=suggestion,name=name,email=email,subject=subject).save()
        data = {
            'form_status':'success'
        }
        print("done")
        return JsonResponse(data,status=200)
    return redirect('home')
