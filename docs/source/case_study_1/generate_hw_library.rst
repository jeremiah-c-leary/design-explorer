Generate HW Library
===================

We have five devices we in our system and we were given which parts will be used:

===========  =================  ============
Device       Manufacturer       Part Number
===========  =================  ============
ADC          Analog Devices     AD4110-1
Temp Sensor  Analog Devices     LTC2986
LED          Lite On            `LTA-1000G <http://optoelectronics.liteon.com/upload/download/DS-30-92-0809/A1000G.pdf>`_
Host         Texas Instruments  OMAP-L137
Discretes    N/A                N/A
Clock Gen    IDT                MK2771-16
===========  =================  ============

Hardware Library Directory Structure
------------------------------------

We will create a hardware library with the following format:

#. hw_lib
   #. adc
      #. analog_devices
         #. ad4110_1
   #. temp_sensor
      #. analog_devices
         #. ltc2986
   #. led
      #. lite_on
         #. lta_1000g
   #. omap
      #. texas_instruments
         #. omap_l137
   #. clock
      #. idt
         #. mk2771_16

For each directory we will add a blank *__init__.py* file.

.. include:: ltc_1000g.rst

