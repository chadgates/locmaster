from django.shortcuts import render
from unlocode.models import LocChangeIndicator, LocFunction, LocStatus, Country, SubDivision
import csv, os
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse


def addLocChangeIndicator(changecode, description):
    locchangeindicator = LocChangeIndicator.objects.get_or_create(changecode=changecode, description=description)[0]
    locchangeindicator.save()
    return locchangeindicator


def addLocFunction(functioncode, description):
    locFunction = LocFunction.objects.get_or_create(functioncode=functioncode, description=description)[0]
    locFunction.save()
    return locFunction


def addLocStatus(statuscode, description):
    locstatus = LocStatus.objects.get_or_create(statuscode=statuscode, description=description)[0]
    locstatus.save()
    return locstatus


def populateInitial(request):
    addLocChangeIndicator("+", "added entry")
    addLocChangeIndicator("#", "Change in the location name")
    addLocChangeIndicator("X", "entry  to be removed in the next issue")
    addLocChangeIndicator("|", "entry has been changed")
    addLocChangeIndicator("=", "reference entry")
    addLocChangeIndicator("!", "US locations with duplicate IATA code, under review")

    addLocFunction("0",
                   "A value 0 in the first position specifies that the functional use of a location is not known and is to be specified")
    addLocFunction("1", "Specifies that the location is a Port, as defined in UN/ECE Recommendation 16.")
    addLocFunction("2", "Specifies that the location is a Rail terminal.")
    addLocFunction("3", "Specifies that the location is a Road terminal.")
    addLocFunction("4", "Specifies that the location is an Airport.")
    addLocFunction("5", "Specifies that the location is a Postal exchange office.")
    addLocFunction("6", "Value reserved for multimodal functions, ICDs etc.")
    addLocFunction("7", "Value reserved for fixed transport functions (e.g. oil platform).")
    addLocFunction("B", "Specifies that the location is Border crossing.")

    addLocStatus("AA", "Approved by competent national government agency")
    addLocStatus("AC", "Approved by Customs Authority")
    addLocStatus("AF", "Approved by national facilitation body")
    addLocStatus("AI", "Code adopted by international organisation (IATA or ECLAC)")
    addLocStatus("AS", "Approved by national standardisation body")
    addLocStatus("RL",
                 "Recognised location - Existence and representation of location name confirmed by check against nominated gazetteer or other reference work")
    addLocStatus("RN", "Request from credible national sources for locations in their own country")
    addLocStatus("RQ", "Request under consideration")
    addLocStatus("RR", "Request rejected")
    addLocStatus("QQ", "Original entry not verified since date indicated")
    addLocStatus("XX", "Entry that will be removed from the next issue of UN/LOCODE")

    return render(request, 'unlocode/populate.html')


def importsubdivisons(request):

    csv_filepathname= os.getcwd()+ "/unlocode/data/subdivisions.txt"
    dataReader = csv.reader(open(csv_filepathname, encoding='utf-8'), dialect='excel-tab')
    #dataReader = csv.reader(open(csv_filepathname), delimter=',', quotechar='"')

    rowcounter = 0
    for row in dataReader:
        if not rowcounter == 0:
            subdivision = SubDivision()
            subdivision.level1 = row[0]
            subdivision.level2 = row[1]
            subdivision.name = row[2]
            subdivision.alpha2code = (subdivision.level1 + subdivision.level2).split("-",1)[0]
            subdivision.shortcode = (subdivision.level1 + subdivision.level2).split("-",1)[1]
            subdivision.save()

        rowcounter += 1

    return HttpResponse( str(rowcounter) + " subdivisions imported")


def importcountries(request):

    csv_filepathname= os.getcwd() + "/unlocode/data/Country_List_ISO_3166_Codes_Latitude_Longitude.csv"

    dataReader = csv.reader(open(csv_filepathname,encoding='utf-8'), delimiter=',', quotechar='"')

    rowcounter = 0
    for row in dataReader:
        if not rowcounter == 0:
            country = Country()
            country.name = row[0]
            country.alpha2code = row[1]
            country.alpha3code = row[2]
            country.numericcode = row[3]
            country.latitudeavg = row[4]
            country.longitudeavg = row[5]
            country.save()

        rowcounter += 1

    return HttpResponse( str(rowcounter) + " countries imported")
