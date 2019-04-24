import design_explorer as de


oInputDiscrete = de.interface.create('Input Discretes')
oInputDiscrete.add_port(de.port.create('DIN', 8, False))

oOutputDiscrete = de.interface.create('Output Discretes')
oOutputDiscrete.add_port(de.port.create('DIN', 8, True))

