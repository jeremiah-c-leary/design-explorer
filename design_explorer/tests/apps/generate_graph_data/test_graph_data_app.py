

import unittest
import design_explorer as de

class test_app(unittest.TestCase):

    def test_simple_graph(self):

        oCca = de.hw.cca.create('cca')

        oComp1 = de.component.create('Comp1')
        oComp2 = de.component.create('Comp2')
        oComp3 = de.component.create('Comp3')
        oComp4 = de.component.create('Comp4')
        oComp5 = de.component.create('Comp5')

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
         
if __name__ == '__main__':
    unittest.main()
