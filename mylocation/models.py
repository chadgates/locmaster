from django.contrib.gis.db import models
import uuid
import re
from django.core.urlresolvers import reverse


# Create your models here.
# This is an auto-generated Django model module created by ogrinspect.

class TimeStampedModel(models.Model):
    # Abstract base class model that provides self-updating created and modified fields
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Unlocode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    locode = models.CharField(max_length=5)
    version = models.CharField(max_length=6)
    lon = models.FloatField()
    lat = models.FloatField()
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    subdivision = models.CharField(max_length=100)
    functions = models.CharField(max_length=8)
    f_port = models.BooleanField(default=False)
    f_rail = models.BooleanField(default=False)
    f_road = models.BooleanField(default=False)
    f_airport = models.BooleanField(default=False)
    f_postal = models.BooleanField(default=False)
    f_multimodal = models.BooleanField(default=False)
    f_fixed = models.BooleanField(default=False)
    f_border = models.BooleanField(default=False)
    lon_dms = models.CharField(max_length=15)
    lat_dms = models.CharField(max_length=15)
    uncoord = models.CharField(max_length=12)

    def save(self, *args, **kwargs):
        # 4. Function code (FUNCTION, mandatory, an8), as follows (with table presentation within brackets):
        # Function          Description                                                 Representation
        # 0                 Function not known, to be specified                         (0-------)
        # 1                 Port, as defined in Rec. 16                                 (1-------)
        # 2                 Rail terminal                                               (-2------)
        # 3                 Road terminal                                               (--3-----)
        # 4                 Airport                                                     (---4----)
        # 5                 Postal exchange office                                      (----5---)
        # [6]               Reserved for Multimodal functions, ICDs, etc.               (-----6--)
        # [7]               Reserved for fixed transport functions (e.g. Oil platform)  (------7-)
        # B                 Border crossing                                             (-------B)
        # If a location has more than one function, include all relevant codes in the function code.
        # Example: for a location with maritime, rail and air functions, assign the code 12-4-
        self.f_port = self.function[0] = '1'
        self.f_rail = self.function[1] = '2'
        self.f_road = self.function[2] = '3'
        self.f_airport = self.function[3] = '4'
        self.f_postal = self.function[4] = '5'
        self.f_multimodal = self.function[5] = '6'
        self.f_fixed = self.function[6] = '7'
        self.f_border = self.function[7] = 'B'
        self.lat_dms, self.lon_dms = unloccoord2dms(self.uncoord)
        self.lat, self.lon = unlocdms2dec(self.lat_dms, self.lon_dms)
        super(Unlocode, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Function(TimeStampedModel):
    code = models.CharField(max_length=10, unique=True, primary_key=True)
    description = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("mylocation:function-detail", kwargs={'pk': self.pk})


class Location(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    point = models.PointField(srid=4326)
    area = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name


class LocationFunction(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False)
    function = models.ForeignKey(Function, on_delete=models.CASCADE, null=False)

    class Meta:
        abstract = True


class LocodeLocation(LocationFunction):
    locode = models.ForeignKey(Unlocode, on_delete=models.CASCADE, null=False)
    f_port = models.BooleanField(default=False)
    f_rail = models.BooleanField(default=False)
    f_road = models.BooleanField(default=False)
    f_airport = models.BooleanField(default=False)
    f_postal = models.BooleanField(default=False)
    f_multimodal = models.BooleanField(default=False)
    f_fixed = models.BooleanField(default=False)
    f_border = models.BooleanField(default=False)
    # rel_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='+')


# class AddressLocation(LocationFunction):
#    pass


class MylocationTest(models.Model):
    description = models.CharField(max_length=20)
    mpoly = models.MultiPolygonField()


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):  # __unicode__ on Python 2
        return self.name


"""
Converting Degrees, Minutes, Seconds formatted coordinate strings to decimal.
Formula:
DEC = (DEG + (MIN * 1/60) + (SEC * 1/60 * 1/60))
Assumes S/W are negative.
"""


def dms2dec(dms_str):
    # Return decimal representation of DMS
    # dms2dec(utf8(48°53'10.18"N))
    # 48.8866111111F
    # dms2dec(utf8(2°20'35.09"E))
    # 2.34330555556F
    # >>> dms2dec(utf8(48°53'10.18"S))
    # -48.8866111111F
    # >>> dms2dec(utf8(2°20'35.09"W))
    # -2.34330555556F

    # Clean all whitespaces
    dms_str = re.sub(r'\s', '', dms_str)

    if re.search('[swSWoO-]', dms_str):
        sign = -1
    else:
        sign = 1

    # TODO::Try use the following regular expression (?![\.,])\D+ instead
    (degree, minute, second, frac_seconds, junk) = re.split('\D+', dms_str, maxsplit=4)

    return sign * (int(degree) + float(minute) / 60 + float(second) / 3600 + float(frac_seconds) / 36000)


def unlocdms2dec(lat_dms, lon_dms):
    if lat_dms and lon_dms:
        latitude = dms2dec(lat_dms)
        longitude = dms2dec(lon_dms)
        return latitude, longitude
    return None, None


def unloccoord2dms(coord_str):
    if re.search('[swneSWNE]', coord_str):
        latitude = coord_str[0:1] + "°" + coord_str[2:3] + "'00.00" + "\"" + coord_str[4]
        longitude = coord_str[6:8] + "°" + coord_str[9:10] + "'00.00" + "\"" + coord_str[11]
        return latitude, longitude
    return None
