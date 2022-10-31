from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def dashboard(request,uname):
    # return HttpResponse(uname)
    context = {
        "uname":uname
    }
    return render(request,"dashboard.html",context)


def basicinfo(request,uname):
    uname = "pradip"
    context = {
        "uname":uname
    }
    return render(request,"basicinfo.html",context)

def socialmedia(request,uname):
    uname = "pradip"
    context = {
        "uname":uname
    }
    return render(request,"socialmedia.html",context)

def aboutme(request,uname):
    uname = "pradip"
    context = {
        "uname":uname
    }
    return render(request,"aboutme.html",context)