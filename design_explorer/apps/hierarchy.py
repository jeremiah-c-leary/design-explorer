
import design_explorer as de


def extract(oSystem):

    lReturn = []

    sLevel = oSystem.name
    lReturn.append(sLevel)

    lComponents = oSystem.components

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
