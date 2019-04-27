

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
        lExpected.append('Comp1, Comp1')
        lExpected.append('Comp2, Comp2')
        lExpected.append('Comp3, Comp3')
        lExpected.append('Comp4, Comp4')
        lExpected.append('Comp5, Comp5')

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

if __name__ == '__main__':
    unittest.main()
