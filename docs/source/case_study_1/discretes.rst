Discretes
---------

The input and output discretes are routed to a connector on the CCA.
So in this case, we will use a generic model of input and output discretes.

.. code-block:: bash

    mkdir -p hw_lib/generic/discretes

We will create or modify the necessary *__init__.py* files at each level of the hierarchy.

hw_lib/__init__.py
^^^^^^^^^^^^^^^^^^

Adding the *generic* directory to the hw_lib init file:

.. code-block:: python

   from . import led
   from . import temp_sensor
   from . import clock
   from . import adc
   from . import processor
   from . import generic 

hw_lib/generic/__init__.py
^^^^^^^^^^^^^^^^^^^^^^^^^^

Creating the *generic* init file:

.. code-block:: python

   from . import discretes

hw_lib/generic/discretes/__init__.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creating the *discretes* init file:

.. code-block:: python

   from . import interfaces
   from .part import *

hw_lib/generic/discretes/interfaces.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Discretes are simple input or output signals.
We will model each with a different interface.
Each interface will contain 8 discretes.

.. code-block:: python

   import design_explorer as de

   
   oInputDiscrete = de.interface.create('Input Discretes')
   oInputDiscrete.add_port(de.port.create('DIN', 8, False))

   oOutputDiscrete = de.interface.create('Output Discretes')
   oOutputDiscrete.add_port(de.port.create('DIN', 8, True))


hw_lib/generic/discretes/part.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The model of the discretes are similar to the other models.

.. code-block:: python

    from . import interfaces
    import design_explorer as de
    
    def create (self):
    
        oReturn = de.component.create('Discretes')
    
        oReturn.add_interface(interfaces.oInputDiscrete)
        oReturn.add_interface(interfaces.oOutputDiscrete)

        return oReturn

