from django.contrib import admin
from .models import Profile, Profile2, Friend, Applicant2


admin.site.register(Profile)
# Register your models here.
admin.site.register(Profile2)
admin.site.register(Friend)
admin.site.register(Applicant2)