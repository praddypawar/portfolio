from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import BasicInfo

# Create your views here.
def logout(request):
    if "uname" in request.session:
        del request.session["uname"]

    if "id" in request.session:
        del request.session["id"]

    return redirect("frontend:signin")


def dashboard(request,uname):
    if "uname" not in request.session and "id" not in request.session:
        return redirect("frontend:signin")
    if request.session["uname"] != uname:
        return redirect("frontend:signin")
    user_data = BasicInfo.objects.get(pk=request.session["id"])
    context = {
        "uname":uname,
        "title":"PortfolioBox-dashboard",
        "user_data":user_data
    }
    return render(request,"dashboard.html",context)


def basicinfo(request,uname):
    if "uname" not in request.session and "id" not in request.session:
        return redirect("frontend:signin")
    if request.session["uname"] != uname:
        return redirect("frontend:signin")
    user_data = BasicInfo.objects.get(pk=request.session["id"])

    


    context = {
        "uname":uname,
        "title":"PortfolioBox-basic-info",
        "user_data":user_data
    }
    return render(request,"basicinfo.html",context)

def socialmedia(request,uname):
    uname = "pradip"
    context = {
        "uname":uname,
        "title":"PortfolioBox-social-media"
    }
    return render(request,"socialmedia.html",context)

def aboutme(request,uname):
    uname = "pradip"
    context = {
        "uname":uname,
        "title":"PortfolioBox-about"
    }
    return render(request,"aboutme.html",context)

def resume(request,uname):
    uname = "pradip"
    context = {
        "uname":uname,
        "title":"PortfolioBox-resume"
    }
    return render(request,"resume.html",context)

def services(request,uname):
    uname = "pradip"
    context = {
        "uname":uname,
        "title":"PortfolioBox-services"
    }
    return render(request,"services.html",context)

def skill(request,uname):
    uname = "pradip"
    context = {
        "uname":uname,
        "title":"PortfolioBox-skill"
    }
    return render(request,"skills.html",context)

def work(request,uname):
    uname = "pradip"
    context = {
        "uname":uname,
        "title":"PortfolioBox-work"
    }
    return render(request,"work.html",context)


def post(request,uname):
    uname = "pradip"
    context = {
        "uname":uname,
        "title":"PortfolioBox-post"
    }
    return render(request,"post.html",context)

def hireme(request,uname):
    uname = "pradip"
    context = {
        "uname":uname,
        "title":"PortfolioBox-hireme"
    }
    return render(request,"hireme.html",context)