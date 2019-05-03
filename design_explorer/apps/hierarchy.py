
import design_explorer as de


def extract(oSystem):

    lReturn = []

    de.utils.get_component_paths(oSystem, oSystem.instanceName, lReturn)

    return lReturn


def filter_upto_level(lHierarchy, iLevel):
    lReturn = []
    for sNode in lHierarchy:
        if sNode.count('.') <= iLevel:
            lReturn.append(sNode)
    return lReturn


def extract_end_points(lHierarchy):
    lReturn = []
    for sNode in lHierarchy[::-1]:
        fFound = False
        for sFinalNode in lReturn:
            if sFinalNode.count(sNode) > 0:
                fFound = True
        if not fFound:
            lReturn.append(sNode)

    return lReturn[::-1]


def extract_mid_points(lHierarchy):
    lReturn = []
    lEndPoints = []
    for sNode in lHierarchy[::-1]:
        fFound = False
        for sFinalNode in lEndPoints:
            if sFinalNode.count(sNode) > 0:
                fFound = True
                if sNode not in lReturn:
                    lReturn.append(sNode)
        if not fFound:
            lEndPoints.append(sNode)

    return lReturn[::-1]


def extract_connections(oSystem, lMidPoints):
    lReturn = []
    for sMidPoint in lMidPoints:
        if sMidPoint.count('.') == 0:
            if oSystem.connections is not None:
                lReturn.extend(oSystem.connections)
        else:
            sMidPoint = remove_system_name(sMidPoint)
            oComponent = oSystem.get_component_named(sMidPoint)
            if oComponent.connections is not None:
                lReturn.extend(oComponent.connections)

    return lReturn


def remove_system_name(sString):
    iIndex = sString.find('.')
    return sString[iIndex + 1:]


def update_paths(oSystem, sPath=None):

    if sPath is None:
        sPath = oSystem.name
    else:
        sPath += '.' + oSystem.instanceName

    oSystem.path = sPath

    try:
        for oInterface in oSystem.interfaces:
            oInterface.path = sPath + '.' + oInterface.name
    except:
        pass

    try:
        for oComponent in oSystem.components:
            update_paths(oComponent, sPath)
    except AttributeError:
        pass
