
from . import interfaces
import design_explorer as de


def create (instanceName):

    oReturn = de.component.create('lta_1000g', instanceName)

    oReturn.add_interface(interfaces.oAnode)
    oReturn.add_interface(interfaces.oCathode)

    return oReturn

