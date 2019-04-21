
Add Connections
---------------

Now we connect the component interfaces to the FPGA interfaces.
We will start with the clock and reset interfaces:

.. code-block:: python

   # Connect clock and reset
   oConnection1 = de.connection.create(oClockGen.get_interface_named('Pclock'), oFpga.get_interface_named('Clock'))
   oConnection1.map('Pclock[0]', 'CLK')

   oConnection2 = de.connection.create(oHost.get_interface_named('GPIO0'), oFpga.get_interface_named('Reset'))
   oConnection2.map('GPIO0[2]', 'RESET_N')

Then connect the discrete inputs and outputs:

.. code-block:: python

   # Connect to input and output discretes
   oConnection3 = de.connection.create(oDiscretes.get_interface_named('Output'), oFpga.get_interface_named('Input Discretes'))
   oConnection4 = de.connection.create(oFpga.get_interface_named('Output Discretes', oDiscretes.get_interface_named('Input'))

Next will will connect the LED interface:

.. code-block:: python

   # Connect to LED
   oConnection5 = de.connection.create(oFpga.get_interface_named('LED'), oLED.get_interface_named('Anode'))

Then the host SPI interface:

.. code-block:: python

   # Connect to Host SPI
   oConnection6 = de.connection.create(oHost.get_interface_named('SPI0'), oFpga.get_interface_named('HOST SPI'))
   oConnection6.map('SPI0_SCS_N', 'HOST_CS_N')
   oConnection6.map('SPI0_CLK', 'HOST_SCLK')
   oConnection6.map('SPI0_SIMO', 'HOST_MOSI')
   oConnection6.map('SPI0_SOMI', 'HOST_MISO')

We will connect the temp sensor interfaces:

.. code-block:: python

   # Connect to temp sensor SPI
   oConnection7 = de.connection.create(oFpga.get_interface_named('Temp Sensor SPI'), oTempSensor.get_interface_named('SPI'))

   # Connect to temp sensor reset
   oConnection8 = de.connection.create(oFpga.get_interface_named('Temp Sensor Discretes'), oTempSensor.get_interface_named('Discretes'))
   oConnection8.map('TS_RESET_N', 'TS_RESET_N')

   # Connect to temp sensor interrupt
   oConnection9 = de.connection.create(oTempSensor.get_interface_named('Interrupt'), oFpga.get_interface_named('Temp Sensor Discretes'))
   oConnection9.map('INTERRUPT', 'TS_INT')

Finally we will connect the ADC interfaces:

.. code-block:: python

   # Connect to ADC SPI interface
   oConnection10 = de.connection.create(oFpga.get_interface_named('ADC SPI'), oADC.get_interface_named('SPI'))

   # Connect to ADC discretes
   oConnection11 = de.connection.create(oFpga.get_interface_named('ADC Discretes'), oADC.get_interface_named('Discretes'))

   # Connect to ADC input select
   oConnection11 = de.connection.create(oFpga.get_interface_named('ADC Input Select'), oADC.get_interface_named('Input Select'))
   oConnection11.map('ADC_AIN[2]', 'AIN2')
   oConnection11.map('ADC_AIN[1]', 'AIN1')
   oConnection11.map('ADC_AIN[0]', 'AINCOM')

The final step in connections is to add them to the system 
