#!/usr/bin/env python

import sys
import os

sys.path.append('..')

from design_explorer import hdl
from design_explorer import hw

#Create top level system
oSystem = hdl.subsystem.create('Top Level System')

#Create cca
oCca = hw.cca.create('Development Board')

#Create FPGA and devices it interacts with
oFpga = hw.fpga.create('FPGA')
oCca.add_component(oFpga)
oCca.add_component(hw.component.create('DAC'))
oCca.add_component(hw.component.create('ADC'))
oCca.add_component(hw.component.create('FLASH'))
oCca.add_component(hw.component.create('DDR4'))

#Create blocks
oClockResetBlock = hdl.subblock.create('Clock Reset')
oFpga.add_hdl_block(oClockResetBlock)

oEmifIp = hdl.subblock.create('EMIF')
oFpga.add_hdl_block(oEmifIp)

oFpgaCore = hdl.subsystem.create('FPGA Core')
oFpga.add_hdl_block(oFpgaCore)
