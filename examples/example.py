#!/usr/bin/env python

import sys

sys.path.append('..')

from design_explorer import hdl
from design_explorer import hw
from design_explorer import connect

#Create top level system
oSystem = hdl.subsystem.create('Top Level System')

#Create cca
oCca = hw.cca.create('Development Board')

#Create FPGA and devices it interacts with
oFpga = hw.fpga.create('FPGA')
oCca.add_component(oFpga)
# Add DAC and it's interfaces
oDac = hw.component.create('DAC')
oDacSpiInterface = hdl.interface.create('DAC SPI')
oDac.add_sink_interface(oDacSpiInterface)
oCca.add_component(oDac)
# Add ADC and it's interfaces
oAdc = hw.component.create('ADC')
oAdcSpiInterface = hdl.interface.create('DAC SPI')
oAdc.add_sink_interface(oAdcSpiInterface)
oCca.add_component(oAdc)
# Add Flash and it's interfaces
oFlash = hw.component.create('FLASH')
oFlashDataInterface = hdl.interface.create('FLASH Data')
oFlash.add_sink_interface(oFlashDataInterface)
oCca.add_component(oFlash)
# Add DDR4 and it's interfaces
oDdr4 = hw.component.create('DDR4')
oDdr4DataInterface = hdl.interface.create('DDR4 Data')
oDdr4.add_sink_interface(oDdr4DataInterface)
oCca.add_component(oDdr4)
# Add interfaces to FPGA
oFpga.add_source_interface(oDacSpiInterface)
oFpga.add_source_interface(oAdcSpiInterface)
oFpga.add_source_interface(oFlashDataInterface)
oFpga.add_source_interface(oDdr4DataInterface)

# Add connections
oDacSpiConnection = connect.create('DAC SPI', oFpga.get_interface('DAC SPI'), oDac.get_interface('DAC SPI'))

#Create blocks
oClockResetBlock = hdl.subblock.create('Clock Reset')
oFpga.add_hdl_block(oClockResetBlock)

oEmifIp = hdl.subblock.create('EMIF')
oFpga.add_hdl_block(oEmifIp)

oFpgaCore = hdl.subsystem.create('FPGA Core')
oFpga.add_hdl_block(oFpgaCore)
