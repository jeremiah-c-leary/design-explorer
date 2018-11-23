Design Explorer Example 1
=========================

Objectives
----------

In this example, we will replicate the diagram below:

image:: block_diagram.png

What we know:

  1) The system is composed of a single CCA
  2) There is an FPGA on the CCA
  3) The FPGA communicates with four devices

Strategy
--------

To recreate this system in *design explorer* we will start at the highest level of the design and work our way to the lowest.

  1) Create a system to contain everything
  2) Create the CCA system to contain the parts
  3) Create the hardware components
     a)  ADC
     b)  DAC
     c)  DDR4 memory
     d)  FLASH memory
     e)  FPGA

Keep in mind, we need to stay at as high a level as possible.
We do not get mired in the details of the interfaces.
Keep them generic as possible.
For example, the ADC has three interfaces:  configuration, data, and discretes.
The configuration can be a 3 wire SPI, 4 wire SPI, or I2C. 
The data interface can be LVDS, serial, or JESD204B.
The discrete interface can vary by manufacturer, but typically includes resets and power downs.
The interfaces required will depend on the device chosen.

Each hardware component will have it's own file.
We can then create a library of parts.
This will allow parts to be re-used in other designs

