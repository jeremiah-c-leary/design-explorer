
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
        if sNode.count('.') <= iLevel and sNode.count('.') > 0:
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
