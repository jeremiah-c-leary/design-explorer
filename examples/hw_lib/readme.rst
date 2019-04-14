Hardware Library
================

A hardware library consists of hardware elements which can be used to build a system.
These can represent simple components such as resistors and capitors.
They can also represent complex digital devices such as FPGAs, Memories, and Analog to Digital Converters.

The library can be organized in many different ways:

  1)  based on your company part number
  2)  based on function
  3)  based on manufacturer
  4)  a combination of any of the above

For the examples in this project, I will choose 2 and 3.
Organize first by function and then manufacturer.

Each function will be subdirectory under the hardware library.
The manufacturer will then be a directory under each function.

The directory structure will look something like this:

  1)  hw_lib
      __init__.py
      a)  ADC
          __init__.py
          1)  Analog_Devices
              __init__.py
              AD7348.py
      b)  DAC
          __init__.py
          1)  Texas_Instruments
              __init__.py
              DAC4523.py

Creating the hardware libray
----------------------------

The first step to creating the hardware library is to create the directory and the *__init__.py* file.

.. code-block:: bash

    $ mkdir hw_lib
    $ touch hw_lib/__init__.py

Creating a function directory
-----------------------------

The function directory I will use to collection devices which perform the same function.
For example, all Analog to Digital converters will be in a directory named **ADC**.
All Digital to Analog converters will be in a directory name **DAC**.
These directories can be further divided as needed.

Creating the function directory follows the same steps as creating a hardware libary:

.. code-block:: bash

    $ mkdir hw_lib/adc
    $ touch hw_lib/adc/__init__.py

However, we need to modify the *hw_lib/__init__.py* file to include the new subdirectory:

.. code-block:: python

    from . import adc

This will allow use to use dot referencing to push into the different levels of the hardware library.

Creating a generic function
---------------------------

In the function directory, we will create a file named *generic.py*.
This will contain a simple interface model of the function.
We can then use this simple model to create an initial system.

First we need to import design_explorer:

.. code-block:: python

    import design_explorer as de

Then we will make a function to return an object which will represent our generic ADC.

.. code-block:: python

    import design_explorer as de


    def create():

We will create a component object...

.. code-block:: python

    import design_explorer as de


    def create():

        oGeneric = de.component.create('ADC')

The next step is to create the interfaces on the ADC.
Given the wide variety of ADCs and differences in their interfaces, we will choose three: Data, Configuration, and Discrete.
The configuration can be a 3 wire SPI, 4 wire SPI, or I2C. 
The data interface can be LVDS, serial, or JESD204B.
The discrete interface will vary by manufacturer, but typically includes resets and power downs.
These interfaces are intended to cover most ADCs.

.. code-block:: python

    import design_explorer as de


    def create():

        oGeneric = de.component.create('ADC')

        oDataInterface = de.interface.create('Data')
        oControlInterface = de.interface.create('Control')
        oDiscreteInterface = de.interface.create('Discrete')

Then we will add the interfaces to the generic object...

.. code-block:: python

    import design_explorer as de


    def create():

        oGeneric = de.component.create('ADC')

        oDataInterface = de.interface.create('Data')
        oControlInterface = de.interface.create('Control')
        oDiscreteInterface = de.interface.create('Discrete')

        oGeneric.add_source_interface(oDataInterface)
        oGeneric.add_sink_interface(oControlInterface)
        oGeneric.add_sink_interface(oDiscreteInterface)

...and then return the object to the caller:

.. code-block:: python

    import design_explorer as de


    def create():

        oGeneric = de.component.create('ADC')

        oDataInterface = de.interface.create('Data')
        oControlInterface = de.interface.create('Control')
        oDiscreteInterface = de.interface.create('Discrete')

        oGeneric.add_source_interface(oDataInterface)
        oGeneric.add_sink_interface(oControlInterface)
        oGeneric.add_sink_interface(oDiscreteInterface)

        return oGeneric
