Host
----

The Host is the Texas Instruments OMAP L137.
Following the LED example, we make the directory.

.. code-block:: bash

    mkdir -p hw_lib/processors/texas_instruments/omap_l137

We will create or modify the necessary *__init__.py* files at each level of the hierarchy.

hw_lib/__init__.py
^^^^^^^^^^^^^^^^^^

Adding the *processor* directory to the hw_lib init file:

.. code-block:: python

   from . import led
   from . import temp_sensor
   from . import clock
   from . import adc
   from . import processor

hw_lib/processor/__init__.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creating the *processor* init file:

.. code-block:: python

   from . import texas_instruments

hw_lib/processor/texas_instruments/__init__.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creating the *texas instruments* init file:

.. code-block:: python

   from . import omap_l137

hw_lib/processor/texas_instruments/omap_l137/__init__.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We add the interfaces and part files to the init file:

.. code-block:: python

   from . import interfaces
   from .part import *

hw_lib/processor/texas_instruments/omap_l137/interfaces.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Previewing the features on page one of the schematic, there are several interfaces: SPI, I2C, UARTs, etc...
For this application, we are only interested in the SPI and GPIO interfaces.

The processor will communicate to the FPGA over SPI.
The pins for the SPI interface are listed in table 3-10 on page 32.
There are two SPI interfaces, but we will be using on SPI0.

The FPGAs reset will be controlled via the GPIO interface.
The GPIO interface is described in section 6.8 on page 76.
We will be using bank 0 of the 8 GPIO banks available.


.. code-block:: python

   import design_explorer as de
   
   oSPI = de.interface.create('SPI0', source=True)
   oSPI.add_port(de.port.create('SPI0_SCS_N', 1, True, 'SPI0 chip select'))
   oSPI.add_port(de.port.create('SPI0_ENA_N', 1, True, 'SPI0 enable'))
   oSPI.add_port(de.port.create('SPI0_CLK', 1, True, 'SPI0 clock'))
   oSPI.add_port(de.port.create('SPI0_SIMO', 1, False, 'SPI0 data slave-in-master-out'))
   oSPI.add_port(de.port.create('SPI0_SOMI', 1, True, 'SPI0 data slave-out-master-in'))

   oGPIO = de.interface.create('GPIO_bank_0', source=True)
   oDiscretes.add_port(de.port.create('GP0', 16, True))


hw_lib/adc/analog_devices/ad4110_1/part.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The model of the omap is similar to the other models.

.. code-block:: python

    from . import interfaces
    import design_explorer as de
    
    def create (self):
    
        oReturn = de.component.create('omap-l137')
    
        oReturn.add_interface(interfaces.oSPI)
        oReturn.add_interface(interfaces.oGPIO0)

        oReturn.datasheet = http://www.ti.com/lit/ds/sprs563g/sprs563g.pdf

        return oReturn

