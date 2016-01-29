from django.db import models

# Create your models here.
class LocChangeIndicator(models.Model):
    locchangeindicator = models.CharField(max_length=1, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class LocFunction(models.Model):
    locfunction = models.CharField(max_length=1, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class LocStatus(models.Model):
    locstatus = models.CharField(max_length=2, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class loccode(models.Model):
    locchangeindicator = models.ForeignKey(LocChangeIndicator)
    loccodecountry = models.CharField(max_length=2)
    loccodeplace = models.CharField(max_length=3)
    locname = models.CharField(max_length=100)
    locnamewodia = models.CharField(max_length=100)
    locsubdivision = models.CharField(max_length=3)
    locfunction = models.CharField(max_length=8)
    locstatus = models.ForeignKey(LocStatus)



    loccode = models.CharField(max_length=5)
