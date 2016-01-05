from .models import *
from django.contrib import admin

class ServerAdmin(admin.ModelAdmin):
    list_display = ('title', 'host', 'port')

admin.site.register(Server, ServerAdmin)
