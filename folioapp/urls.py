from django.urls import path
from . import views

app_name = "frontend"

urlpatterns = [
    path('', views.index,name="index"),
    path("sign-in/",views.signin,name="signin"),
    path("sign-up/",views.signup,name="signup"),
    
]
