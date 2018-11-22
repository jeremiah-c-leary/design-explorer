#!/usr/bin/env python

import sys

sys.path.append('..')

from design_explorer import system
from design_explorer import hdl
from design_explorer import hw
from design_explorer import connect
from design_explorer import utils
from design_explorer import component

#Create top level system
oSystem = system.create('Top Level System')

#Create cca
oCca = hw.cca.create('Development Board')
oSystem.add_component(oCca)

#Create FPGA and devices it interacts with
oFpga = hw.fpga.create('FPGA')
oCca.add_component(oFpga)
# Add DAC and it's interfaces
oDac = component.create('DAC')
oDacSpiInterface = hdl.interface.create('DAC SPI')
oDac.add_sink_interface(oDacSpiInterface)
oCca.add_component(oDac)
# Add ADC and it's interfaces
oAdc = component.create('ADC')
oAdcSpiInterface = hdl.interface.create('DAC SPI')
oAdc.add_sink_interface(oAdcSpiInterface)
oCca.add_component(oAdc)
# Add Flash and it's interfaces
oFlash = component.create('FLASH')
oFlashDataInterface = hdl.interface.create('FLASH Data')
oFlash.add_sink_interface(oFlashDataInterface)
oCca.add_component(oFlash)
# Add DDR4 and it's interfaces
oDdr4 = component.create('DDR4')
oDdr4DataInterface = hdl.interface.create('DDR4 Data')
oDdr4.add_sink_interface(oDdr4DataInterface)
oCca.add_component(oDdr4)
# Add interfaces to FPGA
oFpga.add_source_interface(oDacSpiInterface)
oFpga.add_source_interface(oAdcSpiInterface)
oFpga.add_source_interface(oFlashDataInterface)
oFpga.add_source_interface(oDdr4DataInterface)

# Add connections
oCca.add_connection(connect.create('DAC SPI', oFpga, 'DAC SPI', oDac, 'DAC SPI'))
oCca.add_connection(connect.create('ADC SPI', oFpga, 'ADC SPI', oAdc, 'ADC SPI'))
oCca.add_connection(connect.create('FLASH Data', oFpga, 'FLASH Data', oFlash, 'FLASH Data'))
oCca.add_connection(connect.create('DDR4 Data', oFpga, 'DDR4 Data', oDdr4, 'DDR4 Data'))

#Create blocks
oClockResetBlock = hdl.subblock.create('Clock Reset')
oFpga.add_hdl_block(oClockResetBlock)

oEmifIp = hdl.subblock.create('EMIF')
oFpga.add_hdl_block(oEmifIp)

oFpgaCore = hdl.subsystem.create('FPGA Core')
oFpga.add_hdl_block(oFpgaCore)

#Output node list for gephi
lNodeList = oSystem.extract_node_list()
utils.write_to_file('system_node.csv', lNodeList)

lCcaNodeList = oCca.extract_node_list()
utils.write_to_file('cca_node.csv', lCcaNodeList)
utils.write_to_file('cca_edge.csv', oCca.extract_edge_list())
