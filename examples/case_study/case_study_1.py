
import hw_lib
import design_explorer as de

oSystem = de.system.create('Top level system')

oCCA = de.hw.cca.create('CCA')

oSystem.add_component(oCCA)

# Create components in system
oADC = hw_lib.adc.analog_devices.ad4110_1.create('ADC')
oTempSensor = hw_lib.temp_sensor.analog_devices.ltc2986.create('TempSensor')
oLED = hw_lib.led.lite_on.lta_1000g.create('LED')
oHost = hw_lib.processors.texas_instruments.omap_l137.create('Host')
oClockGen = hw_lib.clock.idt.mk2771_16.create('Clock')
oDiscretes = hw_lib.generic.discretes.create('Discretes')
oFpga = hw_lib.fpga.intel.max10.max10m50.create('FPGA')

oCCA.add_component(oADC)
oCCA.add_component(oTempSensor)
oCCA.add_component(oLED)
oCCA.add_component(oHost)
oCCA.add_component(oClockGen)
oCCA.add_component(oDiscretes)
oCCA.add_component(oFpga)

# Define interface on FPGA

oClock = de.interface.create('Clock')
oClock.create_port('CLK', 1, 'in')

oFpga.add_interface(oClock)

oReset = de.interface.create('Reset')
oReset.create_port('RESET_N', 1, 'in')

oFpga.add_interface(oReset)

oAdcSpiInterface = de.interface.create('ADC SPI')
oAdcSpiInterface.add_port(de.port.create('ADC_CS_N', 1, 'in'))
oAdcSpiInterface.add_port(de.port.create('ADC_SCLK', 1, 'in'))
oAdcSpiInterface.add_port(de.port.create('ADC_MOSI', 1, 'in'))
oAdcSpiInterface.add_port(de.port.create('ADC_MISO', 1, 'out'))

oAdcDiscretes = de.interface.create('ADC Discretes')
oAdcDiscretes.add_port(de.port.create('ADC_SYNC_N', 1, 'out'))
oAdcDiscretes.add_port(de.port.create('ADC_ERR_N', 1, 'out'))
oAdcDiscretes.add_port(de.port.create('ADC_ADR', 2, 'out'))

oAdcInputSelect = de.interface.create('ADC Input Select')
oAdcInputSelect.add_port(de.port.create('ADC_AIN', 3, 'out'))

oFpga.add_interface(oAdcSpiInterface)
oFpga.add_interface(oAdcDiscretes)
oFpga.add_interface(oAdcInputSelect)

oTsSpi = de.interface.create('Temp Sensor SPI')
oTsSpi.add_port(de.port.create('TS_SCLK', 1, 'out'))
oTsSpi.add_port(de.port.create('TS_MOSI', 1, 'out'))
oTsSpi.add_port(de.port.create('TS_CS_N', 1, 'out'))
oTsSpi.add_port(de.port.create('TS_MISO', 1, 'in'))

oTsDiscretes = de.interface.create('Temp Sensor Discretes')
oTsDiscretes.add_port(de.port.create('TS_RESET_N', 1, 'out'))
oTsDiscretes.add_port(de.port.create('TS_INT', 1, 'in'))

oFpga.add_interface(oTsSpi)
oFpga.add_interface(oTsDiscretes)

oLed = de.interface.create('LED')
oLed.create_port('LED', 10, 'out')

oFpga.add_interface(oLed)

oHostSpi = de.interface.create('HOST SPI')
oHostSpi.create_port('HOST_CS_N', 1, 'in')
oHostSpi.create_port('HOST_SCLK', 1, 'in')
oHostSpi.create_port('HOST_MOSI', 1, 'in')
oHostSpi.create_port('HOST_MISO', 1, 'out')
oFpga.add_interface(oHostSpi)

oInputDiscretes = de.interface.create('Input Discretes')
oInputDiscretes.create_port('DISC_IN', 8, 'in')

oOutputDiscretes = de.interface.create('Output Discretes')
oOutputDiscretes.create_port('DISC_OUT', 8, 'out')

oFpga.add_interface(oInputDiscretes)
oFpga.add_interface(oOutputDiscretes)


# Add connections

# Connect clock and reset
oConnection1 = de.connection.create('clock', oClockGen.get_interface_named('PClock'), oFpga.get_interface_named('Clock'), False)
oConnection1.map_port('Pclock[0]', 'CLK')

oConnection2 = de.connection.create('reset', oHost.get_interface_named('GPIO0'), oFpga.get_interface_named('Reset'), False)
oConnection2.map_port('GPIO0[2]', 'RESET_N')

# Connect to input and output discretes
oConnection3 = de.connection.create('discrete inputs', oDiscretes.get_interface_named('Output Discretes'), oFpga.get_interface_named('Input Discretes'))
oConnection4 = de.connection.create('discrete outputs', oFpga.get_interface_named('Output Discretes'), oDiscretes.get_interface_named('Input Discretes'))

# Connect to LED
oConnection5 = de.connection.create('LED', oFpga.get_interface_named('LED'), oLED.get_interface_named('Anode'))

# Connect to Host SPI
oConnection6 = de.connection.create('Host', oHost.get_interface_named('SPI0'), oFpga.get_interface_named('HOST SPI'), False)
oConnection6.map_port('SPI0_SCS_N', 'HOST_CS_N')
oConnection6.map_port('SPI0_CLK', 'HOST_SCLK')
oConnection6.map_port('SPI0_SIMO', 'HOST_MOSI')
oConnection6.map_port('SPI0_SOMI', 'HOST_MISO')

# Connect to temp sensor SPI
oConnection7 = de.connection.create('TS SPI', oFpga.get_interface_named('Temp Sensor SPI'), oTempSensor.get_interface_named('SPI'))

# Connect to temp sensor reset
oConnection8 = de.connection.create('TS Reset', oFpga.get_interface_named('Temp Sensor Discretes'), oTempSensor.get_interface_named('Discretes'), False)
oConnection8.map_port('TS_RESET_N', 'TS_RESET_N')

# Connect to temp sensor interrupt
oConnection9 = de.connection.create('TS Interrupt', oTempSensor.get_interface_named('Interrupt'), oFpga.get_interface_named('Temp Sensor Discretes'), False)
oConnection9.map_port('INTERRUPT', 'TS_INT')

# Connect to ADC SPI interface
oConnection10 = de.connection.create('ADC SPI', oFpga.get_interface_named('ADC SPI'), oADC.get_interface_named('SPI'))

# Connect to ADC discretes
oConnection11 = de.connection.create('ADC Discretes', oFpga.get_interface_named('ADC Discretes'), oADC.get_interface_named('Discretes'))

# Connect to ADC input select
oConnection11 = de.connection.create('ADC Input Select', oFpga.get_interface_named('ADC Input Select'), oADC.get_interface_named('Input Select'), False)
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

