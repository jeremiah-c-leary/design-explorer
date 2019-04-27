
import sys

sys.path.append('../../..')

import design_explorer as de


def create():
    oGeneric = de.component.create('FLASH')

    oDataInterface = de.interface.create('Data')
    oDiscreteInterface = de.interface.create('Discrete')

    oGeneric.add_sink_interface(oDataInterface)
    oGeneric.add_sink_interface(oDiscreteInterface)

    return oGeneric
