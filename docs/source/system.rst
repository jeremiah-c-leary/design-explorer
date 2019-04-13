System
======

A system is a collection of components and/or other systems.

.. image:: img/system.png

The components can represent pieces of HW or FPGAs.
Systems can represent Circuit Card Assemblies (CCA)s, or collections of components.
The system class will be inherited by a multitude of other classes.

Implementation
--------------

We will implement a system as a class:

.. uml:: system_class.uml

Code Examples
-------------

If we were starting from scratch, we could create the above diagram with the following code:

.. code-block:: python

    oSystem = de.system.create('System')
    oSystem.add_component(de.component.create('ADC'))
    oSystem.add_component(de.component.create('DAC'))
    oSystem.add_system(de.system.create('Subsystem1'))
    
    oSubsystem = oSystem.get_system_named('Subsystem1')
    oSubsystem.add_component(de.component.create('Component1'))
    oSubsystem.add_component(de.component.create('Component2'))
    oSubsystem.add_system(de.system.create('Subsystem2'))

    oSubsystem2 = oSubsystem.get_system_named('Subsystem2')
    oSubsystem2.add_component(de.component.create('Component1'))
    oSubsystem2.add_component(de.component.create('Component2'))
    oSubsystem2.add_component(de.component.create('Component3'))

If some of the components already existed, we would just include them:

.. code-block:: python

    oSystem = de.system.create('System')
    oSystem.add_component(hw.lib.adc.analog_devices.create('ADC'))
    oSystem.add_component(hw.lib.dac.texas_instruments.create('DAC'))
    oSystem.add_system(de.system.create('Subsystem1'))
    
    oSubsystem = oSystem.get_system_named('Subsystem1')
    oSubsystem.add_component(de.component.create('Component1'))
    oSubsystem.add_component(de.component.create('Component2'))
    oSubsystem.add_system(my_lib.systems.video_codec.create())

This allows components and systems to be re-used.
It also allows systems to be abstracted.
This will make designing large systems easier and less error prone.

