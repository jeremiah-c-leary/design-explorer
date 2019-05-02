

import unittest
import design_explorer as de

class test_connections(unittest.TestCase):


    def setUp(self):

        self.oSystem = de.system.create('Top Level')

        oCca1 = self.oSystem.add_component(de.hw.cca.create('Cca1'))

        oCca1Comp1 = oCca1.add_component(de.component.create('Comp1', 'Comp1'))
        oCca1Comp1.create_interface('I1')
        oCca1Comp2 = oCca1.add_component(de.component.create('Comp2', 'Comp2'))
        oCca1Comp2.create_interface('I1')
        oCca1Comp3 = oCca1.add_component(de.component.create('Comp3', 'Comp3'))
        oCca1Comp3.create_interface('I1')

        oCca2 = self.oSystem.add_component(de.hw.cca.create('Cca2'))
        oCca2Comp1 = oCca2.add_component(de.component.create('Comp1', 'Comp1'))
        oCca2Comp1.create_interface('I1')
        oCca2Comp2 = oCca2.add_component(de.component.create('Comp2', 'Comp2'))
        oCca2Comp2.create_interface('I1')
        oCca2Comp3 = oCca2.add_component(de.component.create('Comp3', 'Comp3'))
        oCca2Comp3.create_interface('I1')

        oCca3 = self.oSystem.add_component(de.hw.cca.create('Cca3'))
        oCca3Comp1 = oCca3.add_component(de.component.create('Comp1', 'Comp1'))
        oCca3Comp1.create_interface('I1')
        oCca3Comp2 = oCca3.add_component(de.component.create('Comp2', 'Comp2'))
        oCca3Comp2.create_interface('I1')
        oCca3Comp3 = oCca3.add_component(de.component.create('Comp3', 'Comp3'))
        oCca3Comp3.create_interface('I1')

        oCca4 = self.oSystem.add_component(de.hw.cca.create('Cca4'))
        oCca4Comp1 = oCca4.add_component(de.component.create('Comp1', 'Comp1'))
        oCca4Comp1.create_interface('I1')
        oCca4Comp2 = oCca4.add_component(de.component.create('Comp2', 'Comp2'))
        oCca4Comp2.create_interface('I1')
        oCca4Comp3 = oCca4.add_component(de.component.create('Comp3', 'Comp3'))
        oCca4Comp3.create_interface('I1')

        self.oCon1 = de.connection.create('con1', oCca1, 'Comp1.I1', 'Comp2.I1', False)
        self.oCon2 = de.connection.create('con2', oCca2, 'Comp1.I1', 'Comp2.I1', False)
        self.oCon3 = de.connection.create('con3', oCca3, 'Comp1.I1', 'Comp2.I1', False)
        self.oCon4 = de.connection.create('con4', oCca3, 'Comp1.I1', 'Comp2.I1', False)
#        self.oCon5 = de.connection.create('con5', self.oSystem, 'Cca1.Comp1.I1', 'Cca2.Comp1.I1', False)

        oCca1.add_connection(self.oCon1)
        oCca2.add_connection(self.oCon2)
        oCca3.add_connection(self.oCon3)
        oCca4.add_connection(self.oCon4)


    def test_multiple_cca_extract(self):

        lHierarchy = de.apps.hierarchy.extract(self.oSystem)

        lMidPoints = de.apps.hierarchy.extract_mid_points(lHierarchy)

        lActual = de.apps.hierarchy.extract_connections(self.oSystem, lMidPoints)
       
        lExpected = []
        lExpected.append(self.oCon1)
        lExpected.append(self.oCon2)
        lExpected.append(self.oCon3)
        lExpected.append(self.oCon4)
 
        self.assertEqual(lExpected, lActual)


if __name__ == '__main__':
    unittest.main()
