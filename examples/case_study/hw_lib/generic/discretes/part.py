from . import interfaces
import design_explorer as de

def create (instanceName):

    oReturn = de.component.create('Discretes', instanceName)

    oReturn.add_interface(interfaces.oInputDiscrete)
    oReturn.add_interface(interfaces.oOutputDiscrete)

    return oReturn

