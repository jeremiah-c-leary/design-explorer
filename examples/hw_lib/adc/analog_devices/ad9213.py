
import sys

sys.path.append('../../../..')

import design_explorer as de


def create():

    oPart = de.hw.part.create('AD9213')
    oPart.manufacturer = 'Analog Devices'
    oPart.partNumber = 'AD9213'

    oDataInterface = de.interface.create('Data')
    oDataInterface.add_source_port(de.port.create('SERDOUT', 16))

    oControlInterface = de.interface.create('Control')
    oControlInterface.add_sink_port(de.port.create('SDIO', 1))
    oControlInterface.add_sink_port(de.port.create('SCLK', 1))
    oControlInterface.add_sink_port(de.port.create('CSB', 1))

    oDiscreteInterface = de.interface.create('Discrete')
    oDiscreteInterface.add_source_port(de.port.create('GPIO', 6))
    oDiscreteInterface.add_source_port(de.port.create('TRIGGER', 1))

    oPart.add_source_interface(oDataInterface)
    oPart.add_sink_interface(oControlInterface)
    oPart.add_sink_interface(oDiscreteInterface)

    return oPart
