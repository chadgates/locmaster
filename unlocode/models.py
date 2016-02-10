from django.db import models
from django.core.urlresolvers import reverse


class TimeStampedModel(models.Model):
    # Abstract base class model that provides self-updating created and modified fields
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LocVersion(TimeStampedModel):

    version = models.CharField(max_length=6, primary_key=True)
    creator = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("unlocode:detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.version


class LocChangeTags(models.Model):

    changetag = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class LocChangeIndicator(models.Model):
    changecode = models.CharField(max_length=1, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class LocFunction(models.Model):
    functioncode = models.CharField(max_length=1, unique=True)
    description = models.CharField(max_length=200)
    version = models.ForeignKey(LocVersion,
                                on_delete=models.CASCADE,
                                blank=False)

    def __str__(self):
        return self.description


class LocStatus(models.Model):
    statuscode = models.CharField(max_length=2, unique=True)
    description = models.CharField(max_length=200)
    version = models.ForeignKey(LocVersion,
                                on_delete=models.CASCADE,
                                blank = False)

    def __str__(self):
        return self.description


class Country(models.Model):
    name = models.CharField(max_length=200)
    alpha2code = models.CharField(max_length=2, unique=True)
    alpha3code = models.CharField(max_length=3, unique=True)
    numericcode = models.CharField(max_length=3, unique=True)
    latitudeavg = models.FloatField()
    longitudeavg = models.FloatField()

    def __str__ (self):
        return self.name

class SubDivision(models.Model):
    name = models.CharField(max_length=100)
    level1 = models.CharField(max_length = 8)
    level2 = models.CharField(max_length= 8)
    shortcode = models.CharField(max_length=5)
    alpha2code = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class LocCountry(models.Model):
    alpha2code = models.CharField(max_length=2)
    name = models.CharField(max_length=200)
    version = models.ForeignKey(LocVersion,
                                on_delete=models.CASCADE,
                                blank=False)

    def __str__(self):
        return self.name


class LocSubdivison(models.Model):
    alpha2code = models.CharField(max_length=2)
    shortcode = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    version = models.ForeignKey(LocVersion,
                                on_delete=models.CASCADE,
                                blank=False)

    def __str_(self):
        return self.name


class Locode(models.Model):

    # as described here: http://www.unece.org/fileadmin/DAM/cefact/locode/Service/LocodeColumn.htm
    # locchangeindicator = models.ForeignKey(LocChangeIndicator,on_delete=models.PROTECT,blank=True,to_field="changecode")
    # locstatus = models.ForeignKey(LocStatus,on_delete=models.PROTECT,to_field="statuscode", blank=True)

    locchangeindicator = models.CharField(max_length=1)
    locodecountry = models.CharField(max_length=2)
    locodeplace = models.CharField(max_length=3)
    locname = models.CharField(max_length=100)
    locnamewodia = models.CharField(max_length=100)
    locsubdivision = models.CharField(max_length=5)
    locfunction = models.CharField(max_length=8)
    locstatus = models.CharField(max_length=2)
    locdate = models.CharField(max_length=4)
    lociata = models.CharField(max_length=3)
    locoordinates = models.CharField(max_length=12)
    locremarks = models.CharField(max_length=100)
    locode = models.CharField(max_length=5)
    version = models.ForeignKey(LocVersion,
                                on_delete=models.CASCADE,
                                blank=False)

    def save(self, *args, **kwargs):
        self.locode = self.locodecountry + self.locodeplace
        super(Locode, self).save(*args, **kwargs)

    def __str__(self):
        return self.locname
