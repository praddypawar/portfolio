from django.shortcuts import redirect, render


# Create your views here.
def index(request):
    return render(request,"index.html")

def signin(request):

    if request.method == "POST":
        uname ="pradip"
        print(uname)
        return redirect("backend:dashboard",uname)
    return render(request,"login.html")

def signup(request):

    if request.method == "POST":
        uname ="pradip"
        print(uname)
        return redirect("backend:dashboard",uname)
    return render(request,"register.html")