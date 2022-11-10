from django.contrib import admin
from .models import BasicInfo,SocialMedia,AboutMe,FolioViews,WorkExperience
# Register your models here.
admin.site.register(BasicInfo)
admin.site.register(SocialMedia)
admin.site.register(AboutMe)
admin.site.register(FolioViews)
admin.site.register(WorkExperience)

