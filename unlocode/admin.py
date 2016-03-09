from django.contrib import admin

# Register your models here.
from unlocode.models import LocStatus, LocChangeIndicator, LocFunction, LocChangeTag, Locode, LocVersion, LocCountry, \
    LocSubdivision

admin.site.register(LocStatus)
admin.site.register(LocChangeIndicator)
admin.site.register(LocFunction)
admin.site.register(LocChangeTag)
admin.site.register(Locode)
admin.site.register(LocVersion)
admin.site.register(LocSubdivision)
admin.site.register(LocCountry)
