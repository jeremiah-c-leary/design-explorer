Components
==========

A component is a basic design unit.
There are many types of components:

- HW parts
- ADC
- DAC
- RAM
- HDL code
- Circuit Card Assembly (CCA)

Components can hold other components.
This allows for hierarchical design.
For example, a CCA component could include an ADC, DAC, and FPGA.
The FPGA would then include HDL components representing the top level HDL file.
The top level HDL file would then include other components.
They can also contain connections, which show how those subcomponents are connected.
Components also provide interfaces.


Implementation
--------------

We will implement the component as a class:

.. uml:: component_class.uml

Code Examples
-------------

.. code-block::python

  oADC = de.hw.adc.create('ADC')
  oDAC = de.hw.dac.analog_devices('DAC')
  ORAM = de.hw.ram.ddr4.micron.create('DDR4')

  oFPGA = de.hw.fpga.altera.arria10.create('SOC FPGA')
  oFPGA.add_component(de.hdl.entity('SOC_FPGA_TOP'))
  oTopHdl = oFpga.get_component_named('SOC_FPGA_TOP')
  oTopHdl.add_interface()
  oTopHdl.add_interface()

  oClockRst = de.hdl.entity('Clock and Reset Control')
  oClockRst.add_interface()
  oClockRst.add_interface()

  oCore = de.hdl.entity('Core')
  oCore.add_interface()
  oCore.add_interface()

  oTopHdl.add_component(oClockRst)
  oTopHdl.add_component(oCore)
