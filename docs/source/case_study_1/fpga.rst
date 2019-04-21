FPGA
----

The FPGA is where our HDL code will reside.
It's interfaces are defined by the other devices it interacts with.
Following the LED example, we make the directory.

.. code-block:: bash

    mkdir -p hw_lib/fpga/intel/max10/max10M50

We will create or modify the necessary *__init__.py* files at each level of the hierarchy.

hw_lib/__init__.py
^^^^^^^^^^^^^^^^^^

Adding the *fpga* directory to the hw_lib init file:

.. code-block:: python

   from . import led
   from . import temp_sensor
   from . import clock
   from . import adc
   from . import processor
   from . import fpga

hw_lib/fpga/__init__.py
^^^^^^^^^^^^^^^^^^^^^^^

Creating the *fpga* init file:

.. code-block:: python

   from . import intel

hw_lib/fpga/intel/__init__.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creating the *intel* init file:

.. code-block:: python

   from . import max10

hw_lib/fpga/intel/max10/__init__.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creating the *max10* init file:

.. code-block:: python

   from . import max10m50

hw_lib/fpga/intel/max10/max10m50/__init__.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For FPGAs, we do not add interfaces.
We only add the part.
The interfaces will be defined when the part is created.

.. code-block:: python

   from . import part

hw_lib/fpga/intel/max10/max10m50/part.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The model of the FPGA does not include interfaces.
Otherwise it is similar to the other models.
It uses a special form of a component called FPGA.
FPGAs can contain HDL code, while other components can not.

.. code-block:: python

    from . import interfaces
    import design_explorer as de
    
    def create (self):
    
        oReturn = de.fpga.create('max10m50')
    
        oReturn.datasheet = https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/hb/max-10/m10_overview.pdf
        return oReturn

