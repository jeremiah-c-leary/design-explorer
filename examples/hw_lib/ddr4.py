
import sys

sys.path.append('../..')

import design_explorer as de

def create():

    generic = de.component.create('DDR4')
    
    oDataInterface = de.interface.create('Data')
    oDiscreteInterface = de.interface.create('Discrete')
    
    generic.add_sink_interface(oDataInterface)
    generic.add_sink_interface(oDiscreteInterface)

