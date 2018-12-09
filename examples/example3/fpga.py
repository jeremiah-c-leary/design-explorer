
import design_explorer as de
import ip as hdl_ip

# Create the top level entity object
oEntity = de.hdl.entity.create('Entity TOP')

# Create top level interfaces
oClockResetInterface = de.interface.create('Clock and Reset')
oInputs = de.interface.create('Inputs')
oOutputs = de.interface.create('Outputs')

oEntity.add_interface(oClockResetInterface)
oEntity.add_interface(oInputs)
oEntity.add_interface(oOutputs)

# Create the IP components
oIpA = hdl_ip.ipa_a.entity.create('U_IP_A')
oIpB = hdl_ip.ipa_a.entity.create('U_IP_B')
oIpC = hdl_ip.ipa_a.entity.create('U_IP_C')

# Add IP components to 
oEntity.add_component(oIpA)
oEntity.add_component(oIpB)
oEntity.add_component(oIpC)

# Add connections
oIpA.connect('Outputs', oIpB.get_interface('Inputs 1'))
oIpC.connect('Outputs', oIpB.get_interface('Inputs 2'))
oIpB.connect('Outputs', oEntity.get_interface('Outputs'))

oEntity.connect('Clock and Reset', oIpA.get_interface('Clock and Reset'))
oEntity.connect('Clock and Reset', oIpB.get_interface('Clock and Reset'))
oEntity.connect('Clock and Reset', oIpC.get_interface('Clock and Reset'))

