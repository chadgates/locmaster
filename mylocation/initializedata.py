from mylocation.models import Function

def addFunction(code, description):
    function = Function.objects.get_or_create(code=code,
                                              description=description)[0]
    function.save()
    return function

def populateInitial():
    # Populate initial unlocode data into the database that is not related to version.

    # LocChangeIndicator
    addFunction("PORT", "A seaport to load and unload cargo from") #shape or coordinate
    addFunction("TERMINAL", "A terminal in a port area") #a shape or coordinate
    addFunction("PORTAREA", "A port area, covering various terminals") #a shape
    addFunction("BERTH", "A berth within a terminal") #a shape
    addFunction("BASIN", "A basin or harbour within a port ") #a shape
    addFunction("ORDERAREA", "An area to describe a location for an order, example, Shenzhen") #a geographical area
    addFunction("ADDRESS", "A specific place used for an address") #usually coordinates, street name, city etc.
    addFunction("BOLLARD", "A specific bollard in a port") #usually coordinate
