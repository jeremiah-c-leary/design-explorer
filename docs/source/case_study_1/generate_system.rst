Generate System
===============

Now we use the hw_lib we just created to construct our top level system.

First we import design_explorer and the hw_lib

.. code-block:: python

   import hw_lib
   import design_explorer as de

Then we will add the system:

.. code-block:: python

   oSystem = de.system.create('Top level system')

.. include:: generate_system/create_cca.rst
.. include:: generate_system/add_components.rst
.. include:: generate_system/define_interfaces_on_fpga.rst
.. include:: generate_system/add_connections.rst
