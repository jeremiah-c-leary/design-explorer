

import unittest
import design_explorer as de

class test_node_generation(unittest.TestCase):

    def test_five_node_list(self):

        oCca = de.hw.cca.create('cca')

        oComp1 = de.component.create('Comp1', 'Comp1')
        oComp2 = de.component.create('Comp2', 'Comp2')
        oComp3 = de.component.create('Comp3', 'Comp3')
        oComp4 = de.component.create('Comp4', 'Comp4')
        oComp5 = de.component.create('Comp5', 'Comp5')

        oCca.add_component(oComp1)
        oCca.add_component(oComp2)
        oCca.add_component(oComp3)
        oCca.add_component(oComp4)
        oCca.add_component(oComp5)

        lExpected = []
        lExpected.append('Id, Label')
        lExpected.append('cca.Comp1, Comp1')
        lExpected.append('cca.Comp2, Comp2')
        lExpected.append('cca.Comp3, Comp3')
        lExpected.append('cca.Comp4, Comp4')
        lExpected.append('cca.Comp5, Comp5')

        self.assertEqual(lExpected, de.apps.generate_graph_data.node_list(oCca))


class test_edge_generation(unittest.TestCase):

    def setUp(self):
        self.oCca = de.hw.cca.create('cca')

        self.oComp1 = de.component.create('Comp1', 'Comp1')
        self.oComp2 = de.component.create('Comp2', 'Comp2')
        self.oComp3 = de.component.create('Comp3', 'Comp3')
        self.oComp4 = de.component.create('Comp4', 'Comp4')
        self.oComp5 = de.component.create('Comp5', 'Comp5')

        self.oCca.add_component(self.oComp1)
        self.oCca.add_component(self.oComp2)
        self.oCca.add_component(self.oComp3)
        self.oCca.add_component(self.oComp4)
        self.oCca.add_component(self.oComp5)

        self.oComp1.create_interface('C1 I1')
        self.oComp1.create_interface('C1 I2')
        self.oComp1.create_interface('C1 I3')
        self.oComp1.create_interface('C1 I4')
        self.oComp2.create_interface('C2 I1')
        self.oComp3.create_interface('C3 I1')
        self.oComp4.create_interface('C4 I1')
        self.oComp5.create_interface('C5 I1')



    def test_five_nodes_with_five_edges(self):

        oConnection1 = de.connection.create('Connection1', self.oCca, 'Comp1.C1 I1', 'Comp2.C2 I1')
        oConnection2 = de.connection.create('Connection1', self.oCca, 'Comp1.C1 I2', 'Comp3.C3 I1')
        oConnection3 = de.connection.create('Connection1', self.oCca, 'Comp1.C1 I3', 'Comp4.C4 I1')
        oConnection4 = de.connection.create('Connection1', self.oCca, 'Comp1.C1 I4', 'Comp5.C5 I1')

        self.oCca.add_connection(oConnection1)
        self.oCca.add_connection(oConnection2)
        self.oCca.add_connection(oConnection3)
        self.oCca.add_connection(oConnection4)

        lExpected = []
        lExpected.append('Source,Target,Type')
        lExpected.append('Comp1,Comp2,Directed')
        lExpected.append('Comp1,Comp3,Directed')
        lExpected.append('Comp1,Comp4,Directed')
        lExpected.append('Comp1,Comp5,Directed')

        self.assertEqual(lExpected, de.apps.generate_graph_data.edge_list(self.oCca))

    def test_multiple_cca(self):

        oSystem = de.system.create('Top Level')

        oCca1 = oSystem.add_component(de.hw.cca.create('Cca1'))

        oCca1Comp1 = oCca1.add_component(de.component.create('Comp1', 'Comp1'))
        oCca1Comp2 = oCca1.add_component(de.component.create('Comp2', 'Comp2'))
        oCca1Comp3 = oCca1.add_component(de.component.create('Comp3', 'Comp3'))

        oCca2 = oSystem.add_component(de.hw.cca.create('Cca2'))
        oCca2Comp1 = oCca2.add_component(de.component.create('Comp1', 'Comp1'))
        oCca2Comp2 = oCca2.add_component(de.component.create('Comp2', 'Comp2'))
        oCca2Comp3 = oCca2.add_component(de.component.create('Comp3', 'Comp3'))

        lExpected = []
        lExpected.append('Id, Label')
        lExpected.append('Top Level.Cca1, Cca1')
        lExpected.append('Top Level.Cca2, Cca2')

        lActual = de.apps.generate_graph_data.node_list(oSystem)

        self.assertEqual(lExpected, lActual)

        lExpected = []
        lExpected.append('Id, Label')
        lExpected.append('Top Level.Cca1.Comp1, Comp1')
        lExpected.append('Top Level.Cca1.Comp2, Comp2')
        lExpected.append('Top Level.Cca1.Comp3, Comp3')
        lExpected.append('Top Level.Cca2.Comp1, Comp1')
        lExpected.append('Top Level.Cca2.Comp2, Comp2')
        lExpected.append('Top Level.Cca2.Comp3, Comp3')

        lActual = de.apps.generate_graph_data.node_list(oSystem, 2)
        self.assertEqual(lExpected, lActual)

if __name__ == '__main__':
    unittest.main()
