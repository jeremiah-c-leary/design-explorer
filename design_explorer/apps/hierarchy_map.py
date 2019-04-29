
import design_explorer as de


def create(oSystem):

    lReturn = []

    sLevel = oSystem.name
    lReturn.append(sLevel)

    lComponents = oSystem.components

    de.utils.get_component_paths(oSystem, oSystem.instanceName, lReturn)

    return lReturn

