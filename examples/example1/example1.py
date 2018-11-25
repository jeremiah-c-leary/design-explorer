
import sys

sys.path.append('../..')
sys.path.append('../')

import design_explorer as de
import hw_lib
import fpga

oSystem = de.system.create('Example 1 System')

oCca = de.hw.cca.create('CCA')

oSystem.add_component(oCca)

oAdc = hw_lib.adc.generic
oDac = hw_lib.dac.generic
oFlash = hw_lib.flash.generic
oDdr4 = hw_lib.ddr4.generic
oFpga = fpga.generic

oCca.add_component(oAdc)
oCca.add_component(oDac)
oCca.add_component(oFlash)
oCca.add_component(oDdr4)
oCca.add_component(oFpga)

oFpga.add_sink_interface(oAdc.get_interface('Data'),'ADC Data')
oFpga.add_source_interface(oAdc.get_interface('Control'), 'ADC SPI')
oFpga.add_source_interface(oAdc.get_interface('Discrete'), 'ADC Discretes')

oFpga.add_source_interface(oDac.get_interface('Data'), 'DAC Data')
oFpga.add_source_interface(oDac.get_interface('Control'), 'DAC SPI')
oFpga.add_source_interface(oDac.get_interface('Discrete'), 'DAC Discretes')

oFpga.add_source_interface(oFlash.get_interface('Data'), 'FLASH Data')
oFpga.add_source_interface(oFlash.get_interface('Discrete'), 'FLASH Discretes')

oFpga.add_source_interface(oDdr4.get_interface('Data'), 'DDR4 Data')
oFpga.add_source_interface(oDdr4.get_interface('Discrete'), 'DDR4 Discretes')

#Add de.connections
oConnection = de.connect.create('ADC SPI')
oConnection.add_source(oFpga,'Control')
oConnection.add_sink(oAdc,'Control')
oCca.add_connection(oConnection)

oConnection = de.connect.create('ADC Data')
oConnection.add_source(oAdc,'Data')
oConnection.add_sink(oFpga,'Data')
oCca.add_connection(oConnection)

oConnection = de.connect.create('ADC Discretes')
oConnection.add_source(oFpga,'Discrete')
oConnection.add_sink(oAdc,'Discrete')
oCca.add_connection(oConnection)


oConnection = de.connect.create('DAC SPI')
oConnection.add_source(oFpga,'Control')
oConnection.add_sink(oDac,'Control')
oCca.add_connection(oConnection)

oConnection = de.connect.create('DAC Data')
oConnection.add_source(oFpga,'Data')
oConnection.add_sink(oDac,'Data')
oCca.add_connection(oConnection)

oConnection = de.connect.create('DAC Discretes')
oConnection.add_source(oFpga,'Discrete')
oConnection.add_sink(oDac,'Discrete')
oCca.add_connection(oConnection)


oConnection = de.connect.create('FLASH Data')
oConnection.add_source(oFpga,'Data')
oConnection.add_sink(oFlash,'Data')
oCca.add_connection(oConnection)

oConnection = de.connect.create('FLASH Discretes')
oConnection.add_source(oFpga,'Discrete')
oConnection.add_sink(oFlash,'Discrete')
oCca.add_connection(oConnection)


oConnection = de.connect.create('DDR4 Data')
oConnection.add_source(oFpga,'Data')
oConnection.add_sink(oDdr4,'Data')
oCca.add_connection(oConnection)

oConnection = de.connect.create('DDR4 Discretes')
oConnection.add_source(oFpga,'Discrete')
oConnection.add_sink(oDdr4,'Discrete')
oCca.add_connection(oConnection)

# Output node list for gephi

lCcaNodeList = oCca.extract_node_list()
de.utils.write_to_file('cca_node.csv', lCcaNodeList)
de.utils.write_to_file('cca_edge.csv', oCca.extract_edge_list())
de.utils.write_to_file('fpga.vhd', oFpga.create_entity())
