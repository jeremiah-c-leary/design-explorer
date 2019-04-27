from . import interfaces
import design_explorer as de


def create (instanceName):

    oReturn = de.component.create('omap-l137', instanceName)

    oReturn.add_interface(interfaces.oSPI)
    oReturn.add_interface(interfaces.oGPIO0)

    oReturn.datasheet = 'http://www.ti.com/lit/ds/sprs563g/sprs563g.pdf'

    return oReturn
