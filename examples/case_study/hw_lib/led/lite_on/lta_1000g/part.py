
from . import interfaces
import design_explorer as de

def create (self):

    oReturn = de.component.create('lta_1000g')

    oReturn.add_interface(interfaces.oAnode)
    oReturn.add_interface(interfaces.oCathode)

    return oReturn

