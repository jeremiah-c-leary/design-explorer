Ports
=====

Ports within an interface can be either a source or a sink.

For example, the SPI interface on the ADC is a four wire SPI interface has the following ports:

===== ====== ========= ================
Port  Width  Polarity   Direction
===== ====== ========= ================
SCK     1       -       Sink
CS_N    1       0       Sink
DIN     1       -       Sink
DOUT    1       -       Source
===== ====== ========= ================

The Input Discretes Interface could be defined as:

====== ====== ========= ================
Port   Width  Polarity   Direction
====== ====== ========= ================
ADR0     1       -       Sink
ADR1     1       -       Sink
AIN1     1       -       Sink
AIN2     1       -       Sink
AINCOM   1       -       Sink
SYNC_N   1       0       Sink
====== ====== ========= ================

The Output Discretes Interface could be defined as:

===== ====== ========= ================
Port  Width  Polarity   Direction
===== ====== ========= ================
ERR_N   1       0       Source
===== ====== ========= ================

Etc....


The SPI interface on the FPGA will more than likely have differently named ports.

===== ====== ========= ================
Port  Width  Polarity   Direction
===== ====== ========= ================
SCK     1       -       Sink
CS_N    1       0       Sink
MOSI    1       -       Sink
MISO    1       -       Source
===== ====== ========= ================

This can happen if we are re-using a design or because of externally imposed naming conventions.

Implementation
--------------

We will implement a port with a class.

.. uml:: port_class.uml

Code Example
------------

.. code-block:: python

   # Create an interface
   oInterface = de.interface.create(name='SPI', source=False)

   # Add ports to interface
   oInterface.add_port(de.hdl.port.create('SCK', 1, None, False, 'SPI Clock'))
   oInterface.add_port(de.hdl.port.create('CS_N', 1, 0, False, 'SPI Chip Select'))
   oInterface.add_port(de.hdl.port.create('DIN', 1, 0, False, 'Data Input'))
   oInterface.add_port(de.hdl.port.create('DOUT', 1, 0, True, 'Data Output'))
   
