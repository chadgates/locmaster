from django.db import models


class LocChangeIndicator(models.Model):
    changecode = models.CharField(max_length=1, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class LocFunction(models.Model):
    functioncode = models.CharField(max_length=1, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class LocStatus(models.Model):
    statuscode = models.CharField(max_length=2, unique=True)
    description = models.CharField(max_length=200)

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





class Locode(models.Model):

    # as described here: http://www.unece.org/fileadmin/DAM/cefact/locode/Service/LocodeColumn.htm

    locchangeindicator = models.CharField(max_length=1)
    #locchangeindicator = models.ForeignKey(LocChangeIndicator,
    #                                       on_delete=models.SET(''),
    #                                       blank=True,
    #                                       related_name='+')
    locodecountry = models.CharField(max_length=2)
    locodeplace = models.CharField(max_length=3)
    locname = models.CharField(max_length=100)
    locnamewodia = models.CharField(max_length=100)
    locsubdivision = models.CharField(max_length=3)
    locfunction = models.CharField(max_length=8)
    locstatus = models.ForeignKey(LocStatus)
    locdate = models.CharField(max_length=4)
    lociata = models.CharField(max_length=3)
    locoordinates = models.CharField(max_length=12)
    locremarks = models.CharField(max_length=100)
    locode = models.CharField(max_length=5)
    locversion = models.CharField(max_length=10, null=True)

    def save(self, *args, **kwargs):
        self.locode = self.locodecountry + self.locodeplace
        super(Locode, self).save(*args, **kwargs)

    def __str__(self):
        return self.locname
