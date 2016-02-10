from django.contrib import admin

# Register your models here.
from unlocode.models import LocStatus, LocChangeIndicator, LocFunction, LocChangeTags, Locode, LocVersion, LocCountry, \
    LocSubdivison

admin.site.register(LocStatus)
admin.site.register(LocChangeIndicator)
admin.site.register(LocFunction)
admin.site.register(LocChangeTags)
admin.site.register(Locode)
admin.site.register(LocVersion)
admin.site.register(LocSubdivison)
admin.site.register(LocCountry)
