from django.contrib import admin

# Register your models here.
from unlocode.models import LocStatus, LocChangeIndicator, LocFunction

admin.site.register(LocStatus)
admin.site.register(LocChangeIndicator)
admin.site.register(LocFunction)
