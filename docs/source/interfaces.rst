Interfaces
==========

Interfaces exist on every component and indicate communication methods between components.
A component can have multiple interfaces.
Each interface must be uniquely named on a component.
Each interface is composed of at least one port.
Each interface is a source on one component and a sink on another.

For example, the AD4110 ADC clock device could be defined with the following interfaces:

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

An FPGA which communicates with the ADC would have the following interfaces:

================ ============
Interface        Direction
================ ============
SPI              Source
Input Discretes  Source
Output Discretes Sink
================ ============

Naming the interfaces clarifies communication between team members.

Implementation
--------------

We will implement a interface using a class.

.. uml:: interface_class.uml

Interface Ports
===============

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


Connections
===========

Connections between interfaces must align the correct ports.
This will be accomplished using a positional and named association methods.
The default will be positional.
The ports will be matched in the two interfaces starting with the first defined.

 
