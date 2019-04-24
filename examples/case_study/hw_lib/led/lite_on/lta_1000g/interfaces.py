
import design_explorer as de

# Add the interface that we would drive to turn on and off the LEDs
oAnode = de.interface.create('Anode')
oAnode.add_port(de.port.create('Anode', 10, False, 'The end that is driven by the user'))

# This is the ground node
oCathode = de.interface.create('Cathode')
oCathode.add_port(de.port.create('Cathode', 10, False, 'The end that is driven to ground'))

