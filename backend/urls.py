
from . import views
from django.urls import path,include

app_name = "backend"
urlpatterns = [
    path("<str:uname>-dashboard/",views.dashboard,name="dashboard"),
    path("<str:uname>-basic-info/",views.basicinfo,name="basicinfo"),
    path("<str:uname>-social-media/",views.socialmedia,name="socialmedia"),
    path("<str:uname>-about-me/",views.aboutme,name="aboutme"),
    path("<str:uname>-resume/",views.resume,name="resume"),
    path("<str:uname>-services/",views.services,name="services"),
    path("<str:uname>-skill/",views.skill,name="skill"),
    path("<str:uname>-work/",views.work,name="work"),
    path("<str:uname>-post/",views.post,name="post"),
    path("<str:uname>-hireme/",views.hireme,name="hireme"),
    path("logout/",views.logout,name="logout"),
]
