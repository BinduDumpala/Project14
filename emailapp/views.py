from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
import random
import requests
class Home(View):
    def get(self,request):
        return render(request,'input.html')
class Send(View):
    def get(self,request):
        subject='Thankyou for contacting us'
        otp=str(random.randint(100000,999999))
        print(otp)
        from_mail=settings.EMAIL_HOST_USER
        email=request.GET["t1"]
        mobno="+91"+request.GET["t2"]

        to_list=[email]
        send_mail(subject,otp,from_mail,to_list,fail_silently=False)
        resp=requests.post('https://textbelt.com/text',{
            'phone':mobno,
            'message':otp,
            'key':'b2ef7371294ba3466145377b9a2ece5085fff51cISwytw4CyZVGDy299VuONU9Fx',
        })
        print(resp.json())
        return HttpResponse("mail sent successfully")

# Create your views here.
