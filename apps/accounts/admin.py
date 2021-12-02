from django.contrib import admin

# Register your models here.


from .models import UserPersona, UserProfile, UserInterest

admin.site.register(UserPersona)
admin.site.register(UserProfile)
admin.site.register(UserInterest)