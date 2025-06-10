from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import Profile


# Register your models here.
admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
    model = Profile
class userAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]

#unregistering the user modle
admin.site.unregister(User)

admin.site.register(User,userAdmin)

# admin.site.register(Profile)


