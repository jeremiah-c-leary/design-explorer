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
  4) Add the hw components to the CCA

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

Step 1 - Create Top Level System
--------------------------------

The first create a file and import design explorer:

..code-block:: python

    import design_explorer as de

I shortened the name of design_explorer to make api calls shorter.

Then create a system object and give it a name:

..code-block:: python

    import design_explorer as de

    oSystem = de.system.create('Example 1 System')

The system is currently empty, which we will remedy in the next step.

Step 2 - Create CCA
-------------------

A CCA is a specialized form of a system.
We will create one and place it in the top level system.

..code-block:: python

    import design_explorer as de

    oSystem = de.system.create('Example 1 System')

    oCca = de.hw.cca.create('CCA')

    oSystem.add_component(oCca)

Step 3A - Create ADC 
--------------------

We will assume we do not know the exact ADC we will be using.
So we will create a generic ADC.

Open a new file called *adc.py* and import **design_explorer**...

..code-block:: python

    import design_explorer as de

... and create the ADC component:

..code-block:: python

    import design_explorer as de

    generic = component.create('ADC')

The generic ADC will have three interfaces:  Data, Control, Discretes.
We will create the interfaces without defining the ports of the interfaces...

..code-block:: python

    import design_explorer as de

    generic = de.component.create('ADC')

    oDataInterface = de.interface.create('Data')
    oControlInterface = de.interface.create('Control')
    oDiscreteInterface = de.interface.create('Discrete')

...and add them to the ADC component

..code-block:: python

    import design_explorer as de

    generic = de.component.create('ADC')

    oDataInterface = de.interface.create('Data')
    oControlInterface = de.interface.create('Control')
    oDiscreteInterface = de.interface.create('Discrete')

    generic.add_source_interface(oDataInterface)
    generic.add_sink_interface(oControlInterface)
    generic.add_sink_interface(oDiscreteInterface)

Step 3B - Create DAC
--------------------

Step 3C - Create FLASH
----------------------

Step 3D - Create DDR4
---------------------

Step 3E - Create FPGA
---------------------

Step 4 - Add HW Components to CCA
---------------------------------

Adding the components we created is as simple as using the *import* command...

..code-block:: python

    import design_explorer as de
    import adc
    import dac
    import flash
    import ddr4
    import fpga

    oSystem = de.system.create('Example 1 System')

    oCca = de.hw.cca.create('CCA')

    oSystem.add_component(oCca)

...and creating objects...

..code-block:: python

    import design_explorer as de
    import adc
    import dac
    import flash
    import ddr4
    import fpga

    oSystem = de.system.create('Example 1 System')

    oCca = de.hw.cca.create('CCA')

    oSystem.add_component(oCca)

    oAdc = adc.generic
    oDac = dac.generic
    oFlash = flash.generic
    oDdr4 = ddr4.generic
    oFpga = fpga.generic

...and then adding them to the CCA:

..code-block:: python

    import design_explorer as de
    import adc
    import dac
    import flash
    import ddr4
    import fpga

    oSystem = de.system.create('Example 1 System')

    oCca = de.hw.cca.create('CCA')

    oSystem.add_component(oCca)

    oAdc = adc.generic
    oDac = dac.generic
    oFlash = flash.generic
    oDdr4 = ddr4.generic
    oFpga = fpga.generic

    oCca.add_component(oAdc)
    oCca.add_component(oDac)
    oCca.add_component(oFlash)
    oCca.add_component(oDdr4)
    oCca.add_component(oFpga)
 
