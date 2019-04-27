
import hw_lib
import design_explorer as de

oSystem = de.system.create('Top level system')

oCCA = de.hw.cca.create('CCA')

oSystem.add_component(oCCA)

# Create components in system
oCCA.add_component(hw_lib.adc.analog_devices.ad4110_1.create('ADC'))
oCCA.add_component(hw_lib.temp_sensor.analog_devices.ltc2986.create('TempSensor'))
oCCA.add_component(hw_lib.led.lite_on.lta_1000g.create('LED'))
oCCA.add_component(hw_lib.processors.texas_instruments.omap_l137.create('Host'))
oCCA.add_component(hw_lib.clock.idt.mk2771_16.create('Clock'))
oCCA.add_component(hw_lib.generic.discretes.create('Discretes'))
oFpga = oCCA.add_component(hw_lib.fpga.intel.max10.max10m50.create('FPGA'))

# Define interfaces on FPGA

oClock = oFpga.create_interface('Clock')
oClock.create_port('CLK', 1, 'in')

oReset = oFpga.create_interface('Reset')
oReset.create_port('RESET_N', 1, 'in')

oAdcSpiInterface = oFpga.create_interface('ADC SPI')
oAdcSpiInterface.add_port(de.port.create('ADC_CS_N', 1, 'in'))
oAdcSpiInterface.add_port(de.port.create('ADC_SCLK', 1, 'in'))
oAdcSpiInterface.add_port(de.port.create('ADC_MOSI', 1, 'in'))
oAdcSpiInterface.add_port(de.port.create('ADC_MISO', 1, 'out'))

oAdcDiscretes = oFpga.create_interface('ADC Discretes')
oAdcDiscretes.add_port(de.port.create('ADC_SYNC_N', 1, 'out'))
oAdcDiscretes.add_port(de.port.create('ADC_ERR_N', 1, 'out'))
oAdcDiscretes.add_port(de.port.create('ADC_ADR', 2, 'out'))

oAdcInputSelect = oFpga.create_interface('ADC Input Select')
oAdcInputSelect.add_port(de.port.create('ADC_AIN', 3, 'out'))

oTsSpi = oFpga.create_interface('Temp Sensor SPI')
oTsSpi.add_port(de.port.create('TS_SCLK', 1, 'out'))
oTsSpi.add_port(de.port.create('TS_MOSI', 1, 'out'))
oTsSpi.add_port(de.port.create('TS_CS_N', 1, 'out'))
oTsSpi.add_port(de.port.create('TS_MISO', 1, 'in'))

oTsDiscretes = oFpga.create_interface('Temp Sensor Discretes')
oTsDiscretes.add_port(de.port.create('TS_RESET_N', 1, 'out'))
oTsDiscretes.add_port(de.port.create('TS_INT', 1, 'in'))

oLed = oFpga.create_interface('LED')
oLed.create_port('LED', 10, 'out')

oHostSpi = oFpga.create_interface('HOST SPI')
oHostSpi.create_port('HOST_CS_N', 1, 'in')
oHostSpi.create_port('HOST_SCLK', 1, 'in')
oHostSpi.create_port('HOST_MOSI', 1, 'in')
oHostSpi.create_port('HOST_MISO', 1, 'out')

oInputDiscretes = oFpga.create_interface('Input Discretes')
oInputDiscretes.create_port('DISC_IN', 8, 'in')

oOutputDiscretes = oFpga.create_interface('Output Discretes')
oOutputDiscretes.create_port('DISC_OUT', 8, 'out')

# Add connections

# Connect clock and reset
oConnection1 = de.connection.create('clock', oCCA, 'Clock.PClock', 'FPGA.Clock', False)
oConnection1.map_port('Pclock[0]', 'CLK')

oConnection2 = de.connection.create('reset', oCCA, 'Host.GPIO_bank_0', 'FPGA.Reset', False)
oConnection2.map_port('GPIO0[2]', 'RESET_N')

# Connect to input and output discretes
oConnection3 = de.connection.create('discrete inputs', oCCA, 'Discretes.Output Discretes', 'FPGA.Input Discretes')
oConnection4 = de.connection.create('discrete outputs', oCCA, 'FPGA.Output Discretes', 'Discretes.Input Discretes')

# Connect to LED
oConnection5 = de.connection.create('LED', oCCA, 'FPGA.LED', 'LED.Anode')

# Connect to Host SPI
oConnection6 = de.connection.create('Host', oCCA, 'Host.SPI0', 'FPGA.HOST SPI', False)
oConnection6.map_port('SPI0_SCS_N', 'HOST_CS_N')
oConnection6.map_port('SPI0_CLK', 'HOST_SCLK')
oConnection6.map_port('SPI0_SIMO', 'HOST_MOSI')
oConnection6.map_port('SPI0_SOMI', 'HOST_MISO')

# Connect to temp sensor SPI
oConnection7 = de.connection.create('TS SPI', oCCA, 'FPGA.Temp Sensor SPI', 'TempSensor.SPI')

# Connect to temp sensor reset
oConnection8 = de.connection.create('TS Reset', oCCA, 'FPGA.Temp Sensor Discretes', 'TempSensor.Discretes', False)
oConnection8.map_port('TS_RESET_N', 'TS_RESET_N')

# Connect to temp sensor interrupt
oConnection9 = de.connection.create('TS Interrupt', oCCA, 'TempSensor.Interrupt', 'FPGA.Temp Sensor Discretes', False)
oConnection9.map_port('INTERRUPT', 'TS_INT')

# Connect to ADC SPI interface
oConnection10 = de.connection.create('ADC SPI', oCCA, 'FPGA.ADC SPI', 'ADC.SPI')

# Connect to ADC discretes
oConnection11 = de.connection.create('ADC Discretes', oCCA, 'FPGA.ADC Discretes', 'ADC.Discretes')

# Connect to ADC input select
oConnection11 = de.connection.create('ADC Input Select', oCCA, 'FPGA.ADC Input Select', 'ADC.Input Select', False)
oConnection11.map_port('ADC_AIN[2]', 'AIN2')
oConnection11.map_port('ADC_AIN[1]', 'AIN1')
oConnection11.map_port('ADC_AIN[0]', 'AINCOM')


# Add connections to the CCA
oCCA.add_connection(oConnection1)
oCCA.add_connection(oConnection2)
oCCA.add_connection(oConnection3)
oCCA.add_connection(oConnection4)
oCCA.add_connection(oConnection5)
oCCA.add_connection(oConnection6)
oCCA.add_connection(oConnection7)
oCCA.add_connection(oConnection8)
oCCA.add_connection(oConnection9)
oCCA.add_connection(oConnection10)
oCCA.add_connection(oConnection11)

# Now do some stuff

lVhdlEntity = de.apps.generate_vhdl_entity(oFpga)
for sString in lVhdlEntity:
    print sString

lNodes = de.apps.generate_graph_data.node_list(oCCA)
for sString in lNodes:
    print sString

lEdges = de.apps.generate_graph_data.edge_list(oCCA)
for sString in lEdges:
    print sString
