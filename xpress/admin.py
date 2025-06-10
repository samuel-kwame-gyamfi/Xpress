from django.contrib import admin
from django.contrib.auth.models import Group,User


# Register your models here.
admin.site.unregister(Group)


class userAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']

#unregistering the user modle
admin.site.unregister(User)

admin.site.register(User,userAdmin)