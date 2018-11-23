Design Explorer Example 2
=========================

Objectives
----------

In this example, we will replicate the diagram below:

image:: block_diagram.png

What we know:

  1) The system is composed of two ccas
  2) There is an FPGA on each CCA
  3) The FPGAs communicate with each other over some kind of interface

Strategy
--------

To recreate this system in *design explorer* we will start at the highest level of the design and work our way to the lowest.

  1) Create a system to contain everything
  2) Create two CCA systems to contain the parts
  3) Create the hardware components
     a)  Ethernet PHY
     b)  USB PHY
     c)  DDR4 memory
     d)  Temperature sensor
     e)  FPGAs

Keep in mind, we need to stay at as high a level as possible.
We do not get mired in the details of the interfaces.
Keep them generic as possible.
For example, the Ethernet PHY has three interfaces: transmit, receive, and configuration.
The configuration is a standard MDIO interface.
However, the transmit and receive can be MII, RMII, GMII, or RGMII.
The choice of interface can be made at a later time.

Each hardware component will be it's own file.
We can create a library of parts.
This will allow these parts to be re-used in other designs

