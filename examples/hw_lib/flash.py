
import sys

sys.path.append('../..')

import design_explorer as de

generic = de.component.create('FLASH')

oDataInterface = de.interface.create('Data')
oDiscreteInterface = de.interface.create('Discrete')

generic.add_sink_interface(oDataInterface)
generic.add_sink_interface(oDiscreteInterface)

