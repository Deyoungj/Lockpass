from django.contrib import admin
from .models import Passwords


class PasswordAdmin(admin.ModelAdmin):

    list_display = ('site_name', 'date_added')




admin.site.register(Passwords)
