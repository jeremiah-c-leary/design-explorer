
import sys

sys.path.append('../..')

import design_explorer as de


def create():
    generic = de.component.create('ADC')
    
    oDataInterface = de.interface.create('Data')
    oControlInterface = de.interface.create('Control')
    oDiscreteInterface = de.interface.create('Discrete')
    
    generic.add_source_interface(oDataInterface)
    generic.add_sink_interface(oControlInterface)
    generic.add_sink_interface(oDiscreteInterface)

    return generic
