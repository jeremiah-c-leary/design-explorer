Generate HW Library
===================

We have five devices we in our system and we were given which parts will be used:

===========  =================  ============
Device       Manufacturer       Part Number
===========  =================  ============
ADC          Analog Devices     `AD4110-1 <https://www.analog.com/media/en/technical-documentation/data-sheets/AD4110-1.pdf>`_
Temp Sensor  Analog Devices     `LTC2986 <https://www.analog.com/media/en/technical-documentation/data-sheets/AD4110-1.pdf>`_
LED          Lite On            `LTA-1000G <http://optoelectronics.liteon.com/upload/download/DS-30-92-0809/A1000G.pdf>`_
Host         Texas Instruments  `OMAP-L137 <http://www.ti.com/lit/ds/sprs563g/sprs563g.pdf>`_
Discretes    N/A                N/A
Clock Gen    IDT                `MK2771-16 <https://www.idt.com/document/dst/mk2771-15-datasheet>`_ 
===========  =================  ============

Hardware Library Directory Structure
------------------------------------

We will create a hardware library with the following format:

::

  hw_lib
  |
  +-- adc
  |   |
  |   +-- analog_devices
  |       |
  |       +-- ad4110_1
  |
  +-- temp_sensor
  |   |
  |   +-- analog_devices
  |       |
  |       +-- ltc2986
  |
  +-- led
  |   |
  |   +-- lite_on
  |       |
  |       +-- lta_1000g
  |
  +-- processors
  |   |
  |   +-- texas_instruments
  |       |
  |       +-- omap_l137
  |
  +-- clock
      |
      +-- idt
          |
          +-- mk2771_16

For each directory we will add a blank *__init__.py* file.

.. include:: lta_1000g.rst
.. include:: ltc_2986.rst
.. include:: mk2771_16.rst
.. include:: adc4110_1.rst
.. include:: omap.rst
