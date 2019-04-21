############################
Design Explorer Case Study 1
############################

**********
Objectives
**********

In this example, we will replicate the diagram below:

.. image:: img/block_diagram_step_1.png

What we know:

#. The system is composed of a single CCA
#. There is an FPGA on the CCA
#. The FPGA communicates with four devices
#. We were given a set of requirements

********
Strategy
********

#. Generate HW library
#. Generate System

   #. Add components
   #. Define interfaces on FPGA
   #. Add connections
   #. Create CCA

#. Decompose Requirements
#. Architect FPGA

.. include::  generate_hw_library.rst
.. include::  generate_system.rst
.. include::  system_level_requirements.rst

