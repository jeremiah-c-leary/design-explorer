from . import interfaces
import design_explorer as de

def create (self):

    oReturn = de.component.create('Discretes')

    oReturn.add_interface(interfaces.oInputDiscrete)
    oReturn.add_interface(interfaces.oOutputDiscrete)

    return oReturn

