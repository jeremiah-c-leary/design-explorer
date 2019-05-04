
import hw_lib
import design_explorer as de

oSystem = de.system.create('top')

oCca1 = oSystem.add_component(de.hw.cca.create('cca1'))
oCca2 = oSystem.add_component(de.hw.cca.create('cca2'))
oCca3 = oSystem.add_component(de.hw.cca.create('cca3'))
oCca4 = oSystem.add_component(de.hw.cca.create('cca4'))

oFpga1 = oCca1.add_component(de.hw.fpga.create('FPGA1', 'FPGA1'))
oFpga2 = oCca1.add_component(de.hw.fpga.create('FPGA2', 'FPGA2'))
oFpga3 = oCca2.add_component(de.hw.fpga.create('FPGA3', 'FPGA3'))
oFpga4 = oCca3.add_component(de.hw.fpga.create('FPGA4', 'FPGA4'))
oFpga5 = oCca4.add_component(de.hw.fpga.create('FPGA5', 'FPGA5'))

oComp1  = oCca1.add_component(de.component.create('Comp1',  'Comp1'))
oComp2  = oCca1.add_component(de.component.create('Comp2',  'Comp2'))
oComp3  = oCca1.add_component(de.component.create('Comp3',  'Comp3'))
oComp4  = oCca2.add_component(de.component.create('Comp4',  'Comp4'))
oComp5  = oCca2.add_component(de.component.create('Comp5',  'Comp5'))
oComp6  = oCca2.add_component(de.component.create('Comp6',  'Comp6'))
oComp7  = oCca2.add_component(de.component.create('Comp7',  'Comp7'))
oComp8  = oCca3.add_component(de.component.create('Comp8',  'Comp8'))
oComp9  = oCca4.add_component(de.component.create('Comp9',  'Comp9'))
oComp10 = oCca4.add_component(de.component.create('Comp10', 'Comp10'))

# Define interfaces on FPGA

oFpga1.create_interface('I1 to comp1')
oFpga1.create_interface('I2 to fpga2')
oFpga1.create_interface('I3 to comp2')

oFpga2.create_interface('I1')
oFpga2.create_interface('I1 to fpga3')
oFpga2.create_interface('I2 to comp2')
oFpga2.create_interface('I3 to fpga4')
oFpga2.create_interface('I4 to comp3')

oFpga3.create_interface('I1')
oFpga3.create_interface('I1 to fpga4')
oFpga3.create_interface('I2 to comp4')
oFpga3.create_interface('I3 to fpga5')
oFpga3.create_interface('I4 to comp5')
oFpga3.create_interface('I5 to comp6')
oFpga3.create_interface('I6 to comp7')

oFpga4.create_interface('I1')
oFpga4.create_interface('I2')
oFpga4.create_interface('I1 to comp8')
oFpga4.create_interface('I1 to comp9')

oFpga5.create_interface('I1')
oFpga5.create_interface('I1 to comp9')
oFpga5.create_interface('I2 to comp10')

# Define interfaces on components
oComp1.create_interface('I1')
oComp1.create_interface('I2')
oComp1.create_interface('I3')

oComp2.create_interface('I1')
oComp2.create_interface('I2')
oComp2.create_interface('I3')

oComp3.create_interface('I1')
oComp3.create_interface('I2')
oComp3.create_interface('I3')

oComp4.create_interface('I1')
oComp4.create_interface('I2')
oComp4.create_interface('I3')

oComp5.create_interface('I1')
oComp5.create_interface('I2')
oComp5.create_interface('I3')

oComp6.create_interface('I1')
oComp6.create_interface('I2')
oComp6.create_interface('I3')

oComp7.create_interface('I1')
oComp7.create_interface('I2')
oComp7.create_interface('I3')

oComp8.create_interface('I1')
oComp8.create_interface('I2')
oComp8.create_interface('I3')

oComp9.create_interface('I1')
oComp9.create_interface('I2')
oComp9.create_interface('I3')

oComp10.create_interface('I1')
oComp10.create_interface('I2')
oComp10.create_interface('I3')

# Add connections

# Add FPGA 1 connections
oCon1 = de.connection.create('con1', oCca1, 'FPGA1.I1 to comp1', 'Comp1.I1', False)
oCon2 = de.connection.create('con2', oCca1, 'FPGA1.I2 to fpga2', 'FPGA2.I1', False)
oCon3 = de.connection.create('con3', oCca1, 'FPGA1.I3 to comp2', 'Comp2.I1', False)

oCon4 = de.connection.create('con4', oSystem, 'cca1.FPGA2.I1 to fpga3', 'cca2.FPGA3.I1', False)
oCon5 = de.connection.create('con5', oCca1, 'FPGA2.I2 to comp2', 'Comp2.I2', False)
oCon6 = de.connection.create('con6', oSystem, 'cca1.FPGA2.I3 to fpga4', 'cca3.FPGA4.I1', False)
oCon7 = de.connection.create('con7', oCca1, 'FPGA2.I4 to comp3', 'Comp3.I1', False)

oCon8  = de.connection.create('con8',  oSystem, 'cca2.FPGA3.I1 to fpga4', 'cca3.FPGA4.I2', False)
oCon9  = de.connection.create('con9',  oCca2, 'FPGA3.I2 to comp4', 'Comp4.I1', False)
oCon10 = de.connection.create('con10', oSystem, 'cca2.FPGA3.I3 to fpga5', 'cca4.FPGA5.I1', False)
oCon11 = de.connection.create('con11', oCca2, 'FPGA3.I4 to comp5', 'Comp5.I1', False)
oCon12 = de.connection.create('con12', oCca2, 'FPGA3.I5 to comp6', 'Comp6.I1', False)
oCon13 = de.connection.create('con13', oCca2, 'FPGA3.I6 to comp7', 'Comp7.I1', False)

oCon14 = de.connection.create('con14', oCca3, 'FPGA4.I1 to comp8', 'Comp8.I1', False)
oCon15 = de.connection.create('con15', oSystem, 'cca3.FPGA4.I1 to comp9', 'cca4.Comp9.I1', False)

oCon16 = de.connection.create('con16', oCca4, 'FPGA5.I1 to comp9', 'Comp9.I2', False)
oCon17 = de.connection.create('con17', oCca4, 'FPGA5.I2 to comp10', 'Comp10.I1', False)


# Add connections to the CCA
oCca1.add_connection(oCon1)
oCca1.add_connection(oCon2)
oCca1.add_connection(oCon3)
oSystem.add_connection(oCon4)
oCca1.add_connection(oCon5)
oSystem.add_connection(oCon6)
oCca1.add_connection(oCon7)
oSystem.add_connection(oCon8)
oCca2.add_connection(oCon9)
oSystem.add_connection(oCon10)
oCca2.add_connection(oCon11)
oCca2.add_connection(oCon12)
oCca2.add_connection(oCon13)
oCca3.add_connection(oCon14)
oSystem.add_connection(oCon15)
oCca4.add_connection(oCon16)
oCca4.add_connection(oCon17)

# Now do some stuff

for i in range (1, 3):

    lNodes = de.apps.generate_graph_data.node_list(oSystem, i)
    de.utils.write_to_file('nodes_' + str(i) + '.csv', lNodes)
    
    lEdges = de.apps.generate_graph_data.edge_list(oSystem, i)
    de.utils.write_to_file('edges_' + str(i) + '.csv', lEdges)
