import design_explorer as de

oSPI = de.interface.create('SPI')
oSPI.add_port(de.port.create('SCK', 1, 'in'))
oSPI.add_port(de.port.create('SDI', 1, 'in'))
oSPI.add_port(de.port.create('CS_N', 1, 'in'))
oSPI.add_port(de.port.create('SDO', 1, 'out'))

oReset = de.interface.create('Discretes')
oReset.add_port(de.port.create('RESET_N', 1, 'in'))

oInterrupt = de.interface.create('Interrupt')
oInterrupt.add_port(de.port.create('INTERRUPT', 1, 'out'))
