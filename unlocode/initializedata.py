from unlocode.models import LocChangeIndicator, LocChangeTags


def addLocChangeIndicator(changecode, description):
    locchangeindicator = LocChangeIndicator.objects.get_or_create(changecode=changecode,
                                                                  description=description)[0]
    locchangeindicator.save()
    return locchangeindicator


def addLocChangeTag(changetag, description):
    locchangetag = LocChangeTags.objects.get_or_create(changetag=changetag,
                                                       description=description)[0]
    locchangetag.save()
    return locchangetag


def populateInitial():
    # Populate initial unlocode data into the database that is not related to version.

    # LocChangeIndicator
    addLocChangeIndicator("+", "added entry")
    addLocChangeIndicator("#", "Change in the location name")
    addLocChangeIndicator("X", "entry  to be removed in the next issue")
    addLocChangeIndicator("|", "entry has been changed")
    addLocChangeIndicator("=", "reference entry")
    addLocChangeIndicator("!", "US locations with duplicate IATA code, under review")

    # LocChangeTag
    addLocChangeTag("@Coo", "Change affecting or adding Coordinates (change indicator \'|\')")
    addLocChangeTag("@Fun", "Change affecting the Function (change indicator \'|\')")
    addLocChangeTag("@Sta", "Change of status (change indicator \'|\')")
    addLocChangeTag("@Sub", "Addition or change of subdivision code (change indicator \'|\')")
    addLocChangeTag("@Nam", "Change in the location name (change indicator \'#\')")
    addLocChangeTag("@Spe", "Correction of spelling of name (change indicator \'#\')")

    return "Data imported"
