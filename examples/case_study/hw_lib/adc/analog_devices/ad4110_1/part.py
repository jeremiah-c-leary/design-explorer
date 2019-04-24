from . import interfaces
import design_explorer as de

def create (self):

    oReturn = de.component.create('ad4110-1')

    oReturn.add_interface(interfaces.oSPI)
    oReturn.add_interface(interfaces.oDiscretes)
    oReturn.add_interface(interfaces.oInputSelect)

    oReturn.datasheet = 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD4110-1.pdf'

    return oReturn

