from django.contrib.gis import admin
from mylocation.models import WorldBorder, MylocationTest, Function

# Register your models here.
admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(MylocationTest, admin.OSMGeoAdmin)
admin.site.register(Function)


