
import sys

sys.path.append('../../..')

import design_explorer as de


def create():

    oGeneric = de.component.create('ADC')
    
    oDataInterface = de.interface.create('Data')
    oControlInterface = de.interface.create('Control')
    oDiscreteInterface = de.interface.create('Discrete')
    
    oGeneric.add_source_interface(oDataInterface)
    oGeneric.add_sink_interface(oControlInterface)
    oGeneric.add_sink_interface(oDiscreteInterface)

    return oGeneric
