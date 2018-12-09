

import design_explorer as de


def entity():

    oEntity = de.hdl.entity('IP_B')

    oInterface1 = de.interface.create('Clock and Reset')
    oInterface2 = de.interface.create('Inputs A')
    oInterface3 = de.interface.create('Inputs B')
    oInterface4 = de.interface.create('Outputs')

    oEntiity.add_interface(oInterface1)
    oEntiity.add_interface(oInterface2)
    oEntiity.add_interface(oInterface3)
    oEntiity.add_interface(oInterface4)

    return oEntity
