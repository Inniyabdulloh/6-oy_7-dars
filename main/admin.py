from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import SocialMedia, HomePageDate, Contact, CustomUser
# Register your models here.

admin.site.register(HomePageDate)
admin.site.register(SocialMedia)
admin.site.register(Contact)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name']
admin.site.register(CustomUser, CustomUserAdmin)