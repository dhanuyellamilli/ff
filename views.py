from django.shortcuts import render
from . import models

# Create your views here.
def appform(request):
    if request.method=='POST':
        name=request.POST['t1']
        mobile=request.POST['t2']
        email=request.POST['t3']
        models.recruitment.objects.create(name=name,mobile=mobile,email=email)
        return render(request,'rtform/thank.html',{'msg':'thankyou for your interest'})
    return render(request,'rtform/appform.html')

