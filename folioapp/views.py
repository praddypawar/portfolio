from django.shortcuts import redirect, render
from django.contrib import messages
from backend.models import BasicInfo,AboutMe,SocialMedia,FolioViews

# Create your views here.
def index(request):
    return render(request,"index.html")

def signin(request):

    if request.method == "POST":
        uname = request.POST.get("uname")
        password= request.POST.get("password")
        if _data := BasicInfo.objects.filter(uname=uname,password=password).values():
            print(list(_data),"-----")
            uname = _data[0]["uname"]
            request.session["uname"] = _data[0]["uname"]
            request.session["id"] = _data[0]["id"]
            return redirect("backend:dashboard",uname)

        else:
            print("Data not found")
        # return redirect("backend:dashboard",uname)
    return render(request,"login.html")

def signup(request):

    if request.method == "POST":
        uname = request.POST.get("uname")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        password = request.POST.get("password")
        country = request.POST.get("country")
        terms = request.POST.get("terms")
        print(uname,email,password,country,terms)
        if gender == "M":
            profile = "profile/male.jpg"
        else:
            profile = "profile/female.png"
        try:
            BasicInfo(uname=uname,email=email,password=password,country=country,gender=gender,profile=profile).save()
            return redirect("signin")
        except Exception as e:
            print("Error",e)
        
        # messages.error(request,"User Name Not Empty")
    return render(request,"register.html")

def portfolio(request,uname):
    
    basicinfo = BasicInfo.objects.get(uname=uname)
    aboutme = AboutMe.objects.filter(user=basicinfo)
    socialmedia = SocialMedia.objects.filter(user=basicinfo)
    if FolioViews.objects.filter(user=basicinfo):
        viewsuser = FolioViews.objects.get(user=basicinfo)
        viewsuser.number=viewsuser.number+1
        viewsuser.save()
    else:
        FolioViews(user=basicinfo,number=1).save()
    context ={
        "title":uname,
        "basicinfo":basicinfo,
        "aboutme":aboutme,
        "socialmedia":socialmedia
    }
    return render(request,"portfolio.html",context)
