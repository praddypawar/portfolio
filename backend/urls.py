
from . import views
from django.urls import path,include

app_name = "backend"
urlpatterns = [
    path("<str:uname>-dashboard/",views.dashboard,name="dashboard"),
    path("<str:uname>-basic-info/",views.basicinfo,name="basicinfo"),
    path("<str:uname>-social-media/",views.socialmedia,name="socialmedia"),
    path("<str:uname>-about-me/",views.aboutme,name="aboutme"),
]
