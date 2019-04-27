import design_explorer as de

oSPI = de.interface.create('SPI')
oSPI.add_port(de.port.create('CS_N', 1, 'in'))
oSPI.add_port(de.port.create('SCLK', 1, 'in'))
oSPI.add_port(de.port.create('DIN', 1, 'in'))
oSPI.add_port(de.port.create('DOUT', 1, 'out'))

oDiscretes = de.interface.create('Discretes')
oDiscretes.add_port(de.port.create('SYNC_N', 1, 'in'))
oDiscretes.add_port(de.port.create('ERR_N', 1, 'out'))
oDiscretes.add_port(de.port.create('ADR', 2, 'in'))

oInputSelect = de.interface.create('Input Select')
oInputSelect.add_port(de.port.create('AIN2', 1, 'in'))
oInputSelect.add_port(de.port.create('AIN1', 1, 'in'))
oInputSelect.add_port(de.port.create('AINCOM', 1, 'in'))

