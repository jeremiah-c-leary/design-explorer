Interfaces
==========

Interfaces exist on every component and indicate communication methods between components.
A component can have multiple interfaces.
Each interface must be uniquely named on a component.
Each interface is composed of at least one port.
Each interface is a source on one component and a sink on another.

For example, the ADC `AD4110 <https://www.analog.com/media/en/technical-documentation/data-sheets/AD4110-1.pdf>`_ could be defined with the following interfaces:

================ ============
Interface        Direction
================ ============
Power            Sink
SPI              Sink
Input Discretes  Sink
Output Discretes Source
Analog Inputs    Sink
Clock            Sink
================ ============

.. image:: img/adc_interfaces.png

An FPGA which communicates with the ADC could have the following interfaces:

================ ============
Interface        Direction
================ ============
SPI              Source
Input Discretes  Sink
Output Discretes Source
================ ============

.. image:: img/fpga_interfaces.png

Naming the interfaces clarifies communication between team members.

Implementation
--------------

We will implement a interface using a class.

.. image:: img/interface_class.png

Code Example
------------

We can define the interfaces for the ADC and the FPGA using DE:

.. code-block:: python

   oAdc = de.component.create()
   oAdc.add_interface(de.interface('Power'))
   oAdc.add_interface(de.interface('SPI'))
   oAdc.add_interface(de.interface('Input Discretes'))
   oAdc.add_interface(de.interface('Output Discretes'))
   oAdc.add_interface(de.interface('Analog Inputs'))
   oAdc.add_interface(de.interface('Clock'))

   oFPGA = de.component.create()
   oSpiInt = oFPGA.create_interface('SPI')
   oInDisc = oFPGA.create_interface('Input Discretes')
   oOutDisc = oFPGA.create_interface('Output Discretes')

.. NOTE:: There are two methods to creating an interface.
  The first method creates the interface and then use the *add_interface* method of the component class.
  The second uses the *create_interface* method of the component class to create the interface.
  The interface will be returned when using the second method.

If we wanted to grab the SPI interface on the oADC object:

.. code-block:: python

  oSpiInterface = oAdc.get_interface_named('SPI')

