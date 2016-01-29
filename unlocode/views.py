from django.shortcuts import render
from unlocode.models import LocChangeIndicator, LocFunction, LocStatus
# Create your views here.


def addLocChangeIndicator(locchangeindicator, description):

    locchangeindicator = LocChangeIndicator.objects.get_or_create(locchangeindicator=locchangeindicator, description=description)
    locchangeindicator.save()
    return locchangeindicator


def addLocFunction(locfunction, description):

    locfunction = LocFunction.objects.get_or_create(locfunction=locfunction, description=description)
    locfunction.save()
    return locfunction

def addLocStatus(locstatus, description):

    locstatus= LocStatus.objects.get_or_create(locstatus=locstatus, description=description)
    locstatus.save()
    return locstatus


def populateInitial(request):

    addLocChangeIndicator("+", "added entry")
    addLocChangeIndicator("#", "Change in the location name")
    addLocChangeIndicator("X", "entry  to be removed in the next issue")
    addLocChangeIndicator("!", "entry has been changed")
    addLocChangeIndicator("=", "reference entry")
    addLocChangeIndicator("!", "US locations with duplicate IATA code, under review")

    addLocFunction("0", "A value 0 in the first position specifies that the functional use of a location is not known and is to be specified")
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
    addLocStatus("RL", "Recognised location - Existence and representation of location name confirmed by check against nominated gazetteer or other reference work")
    addLocStatus("RN", "Request from credible national sources for locations in their own country")
    addLocStatus("RQ", "Request under consideration")
    addLocStatus("RR", "Request rejected")
    addLocStatus("QQ", "Original entry not verified since date indicated")
    addLocStatus("XX", "Entry that will be removed from the next issue of UN/LOCODE")
