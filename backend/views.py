from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import BasicInfo,SocialMedia,AboutMe,FolioViews

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
    if FolioViews.objects.filter(user=user_data):
        d= FolioViews.objects.get(user=user_data)
        user_view=d.number
    else:
        user_view = 0
    context = {
        "uname":uname,
        "title":"PortfolioBox-dashboard",
        "user_data":user_data,
        "url":request.get_host()+"/"+uname+"-portfolio/",
        "user_view":user_view
    }
    return render(request,"dashboard.html",context)

def basicinfo(request,uname):
    if "uname" not in request.session and "id" not in request.session:
        return redirect("frontend:signin")
    if request.session["uname"] != uname:
        return redirect("frontend:signin")
    user_data = BasicInfo.objects.get(pk=request.session["id"])

    if request.method == "POST":
        user_data.fname = request.POST.get("fname") if request.POST.get("fname") else ""
        user_data.lname = request.POST.get("lname") if request.POST.get("lname") else ""
        user_data.mname = request.POST.get("mname") if request.POST.get("mname") else ""
        user_data.gender = request.POST.get("gender") if request.POST.get("gender") else ""

        if len(request.FILES) != 0:
            user_data.profile = request.FILES.get('profile')

        user_data.dob = request.POST.get("dob") if request.POST.get("dob") else ""
        user_data.mobile = request.POST.get("mobile") if request.POST.get("mobile") else ""
        user_data.save()

    context = {
        "uname":uname,
        "title":"PortfolioBox-basic-info",
        "user_data":user_data
    }
    return render(request,"basicinfo.html",context)

def socialmedia(request,uname):
    if "uname" not in request.session and "id" not in request.session:
        return redirect("frontend:signin")
    if request.session["uname"] != uname:
        return redirect("frontend:signin")
    user_data = BasicInfo.objects.get(pk=request.session["id"])
    social_data = SocialMedia.objects.filter(user=user_data).values()
    main_social_data = []
    other_social_data = []
    if len(social_data)>0:
        main_social_data=social_data[0]
        other_social_data=social_data[1:]


    if request.method == "POST":
        socialmedia_name = request.POST.getlist("socialmedia[]")
        link = request.POST.getlist("link[]")
        social_data_list = list(SocialMedia.objects.filter(user=user_data).values("socialmedia_name"))
        main_data = []

        for s in social_data:
            if s["socialmedia_name"] not in socialmedia_name:
                print(s)
                SocialMedia.objects.get(pk=s["id"]).delete()


        for j in range(len(socialmedia_name)):
            if {"socialmedia_name":socialmedia_name[j]} not in social_data_list:
                main_data.append({"socialmedia_name":socialmedia_name[j],"link":link[j]})
        
        model_instances = [SocialMedia(
            user=user_data,
            socialmedia_name=i["socialmedia_name"],
            link=i["link"]
        ) for i in main_data]

        SocialMedia.objects.bulk_create(model_instances, ignore_conflicts=True)
        return redirect("backend:socialmedia",uname)
    context = {
        "uname":uname,
        "title":"PortfolioBox-social-media",
        "user_data":user_data,
        "main_social_data":main_social_data,
        "other_social_data":other_social_data
    }
    return render(request,"socialmedia.html",context)

def aboutme(request,uname):
    if "uname" not in request.session and "id" not in request.session:
        return redirect("frontend:signin")
    if request.session["uname"] != uname:
        return redirect("frontend:signin")
    user_data = BasicInfo.objects.get(pk=request.session["id"])
    aboutme_data = AboutMe.objects.filter(user=user_data).values()
    main_aboutme_data = []
    other_aboutme_data = []
    if len(aboutme_data)>0:
        main_aboutme_data=aboutme_data[0]
        other_aboutme_data=aboutme_data[1:]


    if request.method == "POST":
        aboutme = request.POST.getlist("aboutme[]")
        aboutme_data_list = list(AboutMe.objects.filter(user=user_data).values("aboutme"))
        main_data = []

        for s in aboutme_data:
            if s["aboutme"] not in aboutme:
                # print(s)
                AboutMe.objects.get(pk=s["id"]).delete()


        for j in range(len(aboutme)):
            if {"aboutme":aboutme[j]} not in aboutme_data_list:
                main_data.append({"aboutme":aboutme[j]})
        
        model_instances = [AboutMe(
            user=user_data,
            aboutme=i["aboutme"]
        ) for i in main_data]

        AboutMe.objects.bulk_create(model_instances, ignore_conflicts=True)
        return redirect("backend:aboutme",uname)
    context = {
        "uname":uname,
        "title":"PortfolioBox-about",
        "user_data":user_data,
        "main_aboutme_data":main_aboutme_data,
        "other_aboutme_data":other_aboutme_data

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