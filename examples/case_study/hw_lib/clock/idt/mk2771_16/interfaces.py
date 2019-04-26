import design_explorer as de

oPclock = de.interface.create('PClock') 
oPclock.add_port(de.port.create('PCLOCK', 2, 'out'))

