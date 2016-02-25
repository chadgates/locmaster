from unlocode.models import Country, SubDivision, Locode, LocCountry, LocFunction, LocStatus, LocSubdivision, LocVersion
from unlocode.models import LocChangeIndicator
import os
import csv
import logging
from django.db import IntegrityError, transaction


def saveatomic(object, logger):
    result = False
    try:
        with transaction.atomic():
                object.save()
    except IntegrityError as ex:
        if logger:
            logger.exception(ex)

    return result


def cleanoutVersion(version):

    logger = logging.getLogger(__name__)

    msg = str(Locode.objects.filter(version=version).delete()[0]) + " LocCodes deleted"
    msg += "\n"
    msg += str(LocCountry.objects.filter(version=version).delete()[0]) + " LocCountries deleted"
    msg += "\n"
    msg += str(LocFunction.objects.filter(version=version).delete()[0]) + " LocCodes deleted"
    msg += "\n"
    msg += str(LocStatus.objects.filter(version=version).delete()[0]) + " LocStatus deleted"
    msg += "\n"
    msg += str(LocSubdivision.objects.filter(version=version).delete()[0]) + " LocSubdivisions deleted"

    logger.info(msg)
    return msg


def importUNLOCODE(version):

    logger = logging.getLogger(__name__)

    path = os.getcwd() + "/unlocode/data/versions/" + version + "/"
    logger.info("Start import for " + path)

    if not (False in dict(check_version_dir(version)).values()):
        objversion = LocVersion.objects.get(version=version)
        msg = cleanoutVersion(version)
        msg += "\n"
        msg += importFunctionClassifiers(objversion, version, path)
        msg += "\n"
        msg += importStatusIndicators(objversion, version, path)
        msg += "\n"
        msg += importCountryCodes(objversion, version, path)
        msg += "\n"
        msg += importLocSubdivision(objversion, version, path)
        msg += "\n"
        msg += importCodeList(objversion, version, path)
    else:
        msg = "Nothing imported, files incomplete. "

    logger.info(msg)
    return msg


def importCountryCodes(objversion, version, path):
    logger = logging.getLogger(__name__)
    csv_filepathname = path + "CountryCodes.txt"
    dataReader = csv.reader(open(csv_filepathname, encoding='utf-8'), delimiter=',', quotechar='"')

    savecounter = 0
    skipcounter = 0
    rowcounter = 0
    for row in dataReader:
        locountry = LocCountry()
        locountry.alpha2code = row[0]
        locountry.name = row[1]
        locountry.version = objversion
        #locountry.save()
        if saveatomic(locountry, logger):
            savecounter += 1
        else:
            skipcounter += 1

        rowcounter += 1

    msg = str(rowcounter) + " Country codes (" + version + ") processed: " + str(savecounter) + \
          " created / " + str(skipcounter) + " skipped."

    logger.info(msg)

    return msg


def importFunctionClassifiers(objversion, version, path):
    logger = logging.getLogger(__name__)
    csv_filepathname = path + "FunctionClassifiers.txt"
    dataReader = csv.reader(open(csv_filepathname, encoding='utf-8'), delimiter=',', quotechar='"')

    rowcounter = 0
    skipcounter = 0
    savecounter = 0

    for row in dataReader:
        locfunction = LocFunction()
        locfunction.functioncode = row[0]
        locfunction.description = row[1]
        locfunction.version = objversion
        try:
            with transaction.atomic():
                locfunction.save()
                savecounter += 1
        except IntegrityError as ex:
            logger.exception(ex)
            logger.exception += 1

        rowcounter += 1

    msg = str(rowcounter) + " Function classifiers (" + version + ") processed: " + str(savecounter) + \
          " created / " + str(skipcounter) + " skipped."

    logger.info(msg)

    return msg


def importStatusIndicators(objversion, version, path):
    logger = logging.getLogger(__name__)
    csv_filepathname = path + "StatusIndicators.txt"
    dataReader = csv.reader(open(csv_filepathname, encoding='utf-8'), delimiter=',', quotechar='"')

    rowcounter = 0
    skipcounter = 0
    savecounter = 0

    for row in dataReader:
        locstatus = LocStatus()
        locstatus.statuscode = row[0]
        locstatus.description = row[1]
        locstatus.version = objversion
        try:
            with transaction.atomic():
                locstatus.save()
                savecounter += 1
        except IntegrityError as ex:
            logger.exception(ex)
            skipcounter += 1

        rowcounter += 1

    msg = str(rowcounter) + " Status Indicators (" + version + ") processed: " + str(savecounter) + \
          " created / " + str(skipcounter) + " skipped."

    logger.info(msg)

    return msg


def importLocSubdivision(objversion, version, path):
    logger = logging.getLogger(__name__)
    csv_filepathname = path + "SubdivisionCodes.txt"
    dataReader = csv.reader(open(csv_filepathname, encoding='utf-8'), delimiter=',', quotechar='"')
    rowcounter = 0
    skipcounter = 0
    savecounter = 0
    for row in dataReader:
        locsubdivision = LocSubdivision()
        locsubdivision.alpha2code = LocCountry.objects.filter(alpha2code=row[0], version=version).first()
        locsubdivision.shortcode = row[1]
        locsubdivision.name = row[2]
        locsubdivision.version = objversion
        try:
            with transaction.atomic():
                locsubdivision.save()
                savecounter += 1
        except IntegrityError as ex:
            logger.exception(ex)
            skipcounter += 1

        rowcounter += 1

    msg = str(rowcounter) + " Subdivisions (" + version + ") processed: " + str(savecounter) + \
          " created / " + str(skipcounter) + " skipped."

    logger.info(msg)

    return msg


def importCodeList(objversion, version, path):
    logger = logging.getLogger(__name__)
    csv_filepathname = path + "CodeList.txt"
    dataReader = csv.reader(open(csv_filepathname, encoding='utf-8'), delimiter=',', quotechar='"')

    savecounter = 0
    skipcounter = 0
    rowcounter = 0
    for row in dataReader:
        if row[2] != '':
            locode = Locode()
            locode.locchangeindicator = LocChangeIndicator.objects.filter(changecode=row[0]).first()
            locode.locodecountry = LocCountry.objects.filter(alpha2code=row[1], version=objversion).first()
            locode.locodeplace = row[2]
            locode.locname = row[3]
            locode.locnamewodia = row[4]
            locode.locsubdivision = LocSubdivision.objects.filter(shortcode=row[5], version=objversion,
                                                                  alpha2code=locode.locodecountry_id).first()
            locode.locfunction = row[7]
            locode.locstatus = LocStatus.objects.filter(statuscode=row[6], version=objversion).first()
            locode.locdate = row[8]
            locode.lociata = row[9]
            locode.locoordinates = row[10]
            locode.locremarks = row[11]
            # locode.locode = row[1]+row[2]
            locode.version = objversion
            try:
                with transaction.atomic():
                    locode.save()
                    savecounter += 1
            except IntegrityError as ex:
                logger.exception(ex)
                skipcounter += 1
        else:
            skipcounter += 1

        rowcounter += 1

    msg = str(rowcounter) + " UN/LOCODES (" + version + ") processed: " + str(savecounter) + \
          " created / " + str(skipcounter) + " skipped."

    logger.info(msg)
    return msg


def importsubdivisons():
    logger = logging.getLogger(__name__)
    csv_filepathname = os.getcwd() + "/unlocode/data/subdivisions.txt"
    dataReader = csv.reader(open(csv_filepathname, encoding='utf-8'), dialect='excel-tab')
    # dataReader = csv.reader(open(csv_filepathname), delimter=',', quotechar='"')

    savecounter = 0
    skipcounter = 0
    rowcounter = 0
    for row in dataReader:
        if not rowcounter == 0:
            subdivision = SubDivision()
            subdivision.level1 = row[0]
            subdivision.level2 = row[1]
            subdivision.name = row[2]
            subdivision.alpha2code = (subdivision.level1 + subdivision.level2).split("-", 1)[0]
            subdivision.shortcode = (subdivision.level1 + subdivision.level2).split("-", 1)[1]
            try:
                with transaction.atomic():
                    subdivision.save()
                    savecounter += 1
            except IntegrityError as ex:
                logger.exception(ex)
                skipcounter += 1

        rowcounter += 1

    msg = str(rowcounter) + " Subdivisions processed: " + str(savecounter) + \
          " created / " + str(skipcounter) + " skipped."

    logger.info(msg)
    return msg


def importcountries():
    csv_filepathname = os.getcwd() + "/unlocode/data/Country_List_ISO_3166_Codes_Latitude_Longitude.csv"

    dataReader = csv.reader(open(csv_filepathname, encoding='utf-8'), delimiter=',', quotechar='"')

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

    return str(rowcounter) + " countries imported"


def check_for_complete_set(filelist):
    loc_set = {'CodeList.txt': False,
               'CountryCodes.txt': False,
               'FunctionClassifiers.txt': False,
               'StatusIndicators.txt': False,
               'SubdivisionCodes.txt': False}

    for items in filelist:
        if items in loc_set:
            loc_set.update({items: True})

    return list(loc_set.items())


def get_file_names(directory):
    """Returns list of file names within directory"""
    contents = os.listdir(directory)
    files = list()
    for item in contents:
        if os.path.isfile(os.path.join(directory, item)):
            files.append(item)
    return files


def check_version_dir(version):
    dirpath = os.getcwd() + "/unlocode/data/versions/" + version
    if os.path.exists(dirpath):
        files = get_file_names(dirpath)
    else:
        files = ""
    filestatus = check_for_complete_set(files)
    return filestatus
