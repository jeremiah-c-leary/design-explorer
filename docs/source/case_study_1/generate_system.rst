Generate System
===============

Now we use the hw_lib we just created to construct our top level system.

First we import design_explorer and the hw_lib

.. code-block:: python

   import hw_lib
   import design_explorer as de

Add Components
--------------

We will be creating the components before adding them to the system:

.. code-block:: python

   import hw_lib
   import design_explorer as de

   # Create components in system
   oADC = hw_lib.adc.analog_devices.ad4110_1.create('ADC')
   oTempSensor = hw_lib.temp_sensor.analog_devices.ltc2986.create('TempSensor')
   oLED = hw_lib.led.lite_on.lta_1000g.create('LED')
   oHost = hw_lib.processors.texas_instruments.omap_l137.create('Host')
   oClockGen = hw_lib.clock.idt.mk2771_16.create('Clock')
   oDiscretes = hw_lib.generic.discretes.create('Discretes')
   oFPGA = hw_lib.fpga.intel.max10.max10m50.create('FPGA')

.. NOTE:: There is a lot of information in the above lines.
   Each line explicitely states what the component is.
   Going from left to right it includes the type of device, manufacturer, and part number.
   This condensing of information is part of what design-explorer is designed for.

Define Interfaces on FPGA
-------------------------

The FPGA does not start with any predefined interfaces.
All interfaces are determined by which external HW components it communicates with.

We will start adding interfaces for the ADC:

.. code-block:: python

   oAdcSpiInterface = de.interface.create('ADC SPI', source=True)
   oAdcSpiInterface.add_port(de.port.create('ADC_CS_N', 1, True))
   oAdcSpiInterface.add_port(de.port.create('ADC_SCLK', 1, True))
   oAdcSpiInterface.add_port(de.port.create('ADC_MOSI', 1, True))
   oAdcSpiInterface.add_port(de.port.create('ADC_MISO', 1, False))

   oAdcDiscretes = de.interface.create('ADC Discretes', source=True)
   oAdcDiscretes.add_port(de.port.create('ADC_SYNC_N', 1, True))
   oAdcDiscretes.add_port(de.port.create('ADC_ERR_N', 1, False))
   oAdcDisctetes.add_port(de.port.create('ADC_ADR', 2, True))

   oAdcInputSelect = de.iterface.create('ADC Input Select', source=True)
   oAdcInputSelect.add_port(de.port.create('ADC_AIN2', 1, True))
   oAdcInputSelect.add_port(de.port.create('ADC_AIN1', 1, True))
   oAdcInputSelect.add_port(de.port.create('ADC_AINCOM', 1, True))

   oFpga.add_interface(oAdcSpiInterface)
   oFpga.add_interface(oAdcDiscretes)
   oFpga.add_interface(oAdcInputSelect)

Then we will add interfaces for the temperature sensor:

.. code-block:: python

   oTsSpi = de.interface.create('Temp Sensor SPI', source=True)
   oTsSpi.add_port(de.port.create('TS_SCLK', 1, True))
   oTsSpi.add_port(de.port.create('TS_MOSI', 1, True))
   oTsSpi.add_port(de.port.create('TS_CS_N', 1, True))
   oTsSpi.add_port(de.port.create('TS_MISO', 1, False))

   oTsDiscretes = de.interface.create('Temp Sensor Discretes', source=True)
   oTsDiscretes.add_port(de.port.create('TS_RESET', 1, True))
   oTsDiscretes.add_port(de.port.create('TS_INT', 1, False))

   oFpga.add_interface(oTsSpi)
   oFpga.add_interface(oTsDiscretes)

Now we add an interface for the LED part:

.. code-block:: python

   oLed = de.interface.create('LEDs', source=True)
   oLed.create_port('LED', 10, True)

   oFpga.add_interface(oLed)

Next we add the host interfaces:

.. code-block:: python

   oHostSpi = de.interfaces.create('HOST SPI')
   oHostSpi.create_port('HOST_CS_N', 1, False)
   oHostSpi.create_port('HOST_SCLK', 1, False)
   oHostSpi.create_port('HOST_MOSI', 1, False)
   oHostSpi.create_port('HOST_MISO', 1, True))

   oReset = de.interfaces.create('Reset')
   oReset.create_port('RESET_N', 1, False)

   oFpga.add_interface(oHostSpi)
   oFpga.add_interface(oReset)

Then the interface from the clock device:

.. code-block:: python

   oClock = de.interfaces.create('Clock')
   oClock.create_port('CLK', 1, False)

   oFpga.add_interface(oClock)

Finally we will add the discrete interfaces:

.. code-block:: python

   oInputDiscretes = de.interface.create('Input Discretes')
   oInputDiscretes.create_port('DISC_IN', 8, False)

   outputDiscretes = de.interface.create('Output Discretes')
   outputDiscretes.create_port('DISC_OUT', 8, False)

   oFpga.add_interface(oInputDiscretes)
   oFpga.add_interface(oOutputDiscretes)

.. NOTE:: These interfaces should be defined in a seperate file and imported.
   This will keep the code cleaner

