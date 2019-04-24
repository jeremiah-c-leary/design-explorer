import design_explorer as de

oSPI = de.interface.create('SPI0')
oSPI.add_port(de.port.create('SPI0_SCS_N', 1, True, 'SPI0 chip select'))
oSPI.add_port(de.port.create('SPI0_ENA_N', 1, True, 'SPI0 enable'))
oSPI.add_port(de.port.create('SPI0_CLK', 1, True, 'SPI0 clock'))
oSPI.add_port(de.port.create('SPI0_SIMO', 1, False, 'SPI0 data slave-in-master-out'))
oSPI.add_port(de.port.create('SPI0_SOMI', 1, True, 'SPI0 data slave-out-master-in'))

oGPIO0 = de.interface.create('GPIO_bank_0')
oGPIO0.add_port(de.port.create('GP0', 16, True))

