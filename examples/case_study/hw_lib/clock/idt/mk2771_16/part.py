from . import interfaces
import design_explorer as de

def create (instanceName):

    oReturn = de.component.create('mk2771_16', instanceName)

    oReturn.add_interface(interfaces.oPclock)

    oReturn.datasheet = 'https://www.idt.com/document/dst/mk2771-15-datasheet'

    return oReturn
