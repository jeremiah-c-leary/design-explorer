import design_explorer as de

oSPI = de.interface.create('SPI') 
oSPI.add_port(de.port.create('CS_N', 1, False))
oSPI.add_port(de.port.create('SCLK', 1, False))
oSPI.add_port(de.port.create('DIN', 1, False))
oSPI.add_port(de.port.create('DOUT', 1, True))

oDiscretes = de.interface.create('Discretes') 
oDiscretes.add_port(de.port.create('SYNC_N', 1, False))
oDiscretes.add_port(de.port.create('ERR_N', 1, True))
oDiscretes.add_port(de.port.create('ADR', 2, False))

oInputSelect = de.interface.create('Input Select') 
oInputSelect.add_port(de.port.create('AIN2', 1, False))
oInputSelect.add_port(de.port.create('AIN1', 1, False))
oInputSelect.add_port(de.port.create('AINCOM', 1, False))

