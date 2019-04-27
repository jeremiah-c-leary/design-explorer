from . import interfaces
import design_explorer as de


def create (instanceName):

    oReturn = de.component.create('ltc2986', instanceName)

    oReturn.add_interface(interfaces.oSPI)
    oReturn.add_interface(interfaces.oReset)
    oReturn.add_interface(interfaces.oInterrupt)

    return oReturn
