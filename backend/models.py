from django.db import models
from . import base
from bulk_update_or_create import BulkUpdateOrCreateQuerySet
# Create your models here.

class BasicInfo(base.Base):
    gender_choice = (("M","Male"),("F","Female"),("T","Transgender"))
    uname = models.CharField(max_length=50,unique=True)
    fname = models.CharField(null=False, blank=False,max_length=50)
    mname = models.CharField(null=False, blank=False,max_length=50)
    lname = models.CharField(null=False, blank=False,max_length=50)
    gender = models.CharField(null=False, blank=False,max_length=1,choices=gender_choice)
    profile = models.ImageField(upload_to="profile/")
    dob = models.DateField(null=True, blank=True)
    mobile = models.CharField(null=False, blank=False,max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    country = models.CharField(max_length = 255)


    def __str__(self) -> str:
        return self.uname

class SocialMedia(base.Base):
    user = models.ForeignKey(BasicInfo,on_delete=models.CASCADE)
    socialmedia_name = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    objects = BulkUpdateOrCreateQuerySet.as_manager()
        

class AboutMe(base.Base):
    user = models.ForeignKey(BasicInfo,on_delete=models.CASCADE)
    aboutme = models.TextField()
    objects = BulkUpdateOrCreateQuerySet.as_manager()


class FolioViews(base.Base):
    user = models.ForeignKey(BasicInfo,on_delete=models.CASCADE)
    number = models.BigIntegerField()
        




