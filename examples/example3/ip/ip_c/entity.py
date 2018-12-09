

import design_explorer as de


def entity():

    oEntity = de.hdl.entity('IP_C')

    oInterface1 = de.interface.create('Clock and Reset')
    oInterface2 = de.interface.create('Outputs')

    oEntiity.add_interface(oInterface1)
    oEntiity.add_interface(oInterface2)

    return oEntity
