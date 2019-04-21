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

Then we add them to the CCA:

.. code-block:: python

    oCCA.add_component(oADC)
    oCCA.add_component(oTempSensor)
    oCCA.add_component(oLED)
    oCCA.add_component(oHost)
    oCCA.add_component(oClockGen)
    oCCA.add_component(oDiscretes)
    oCCA.add_component(oFPGA)

