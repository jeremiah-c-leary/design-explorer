from . import interfaces
import design_explorer as de

def create (self):

    oReturn = de.component.create('ltc2986')

    oReturn.add_interface(interfaces.oSPI)
    oReturn.add_interface(interfaces.oReset)
    oReturn.add_interface(interfaces.oInterrupt)

    return oReturn
