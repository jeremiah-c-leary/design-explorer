

import unittest
import design_explorer as de

class test_hierarchy_app(unittest.TestCase):

    def test_single_cca_with_five_components(self):

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
        lExpected.append('cca')
        lExpected.append('cca.Comp1')
        lExpected.append('cca.Comp2')
        lExpected.append('cca.Comp3')
        lExpected.append('cca.Comp4')
        lExpected.append('cca.Comp5')

        self.assertEqual(lExpected, de.apps.hierarchy.extract(oCca))


    def test_multiple_cca_extract(self):

        oSystem = de.system.create('Top Level')

        oCca1 = oSystem.add_component(de.hw.cca.create('Cca1'))

        oCca1Comp1 = oCca1.add_component(de.component.create('Comp1', 'Comp1'))
        oCca1Comp2 = oCca1.add_component(de.component.create('Comp2', 'Comp2'))
        oCca1Comp3 = oCca1.add_component(de.component.create('Comp3', 'Comp3'))

        oCca2 = oSystem.add_component(de.hw.cca.create('Cca2'))
        oCca2Comp1 = oCca2.add_component(de.component.create('Comp1', 'Comp1'))
        oCca2Comp2 = oCca2.add_component(de.component.create('Comp2', 'Comp2'))
        oCca2Comp3 = oCca2.add_component(de.component.create('Comp3', 'Comp3'))

        oCca3 = oSystem.add_component(de.hw.cca.create('Cca3'))
        oCca3Comp1 = oCca3.add_component(de.component.create('Comp1', 'Comp1'))
        oCca3Comp2 = oCca3.add_component(de.component.create('Comp2', 'Comp2'))
        oCca3Comp3 = oCca3.add_component(de.component.create('Comp3', 'Comp3'))

        oCca4 = oCca3.add_component(de.hw.cca.create('Cca4'))
        oCca4Comp1 = oCca4.add_component(de.component.create('Comp1', 'Comp1'))
        oCca4Comp2 = oCca4.add_component(de.component.create('Comp2', 'Comp2'))
        oCca4Comp3 = oCca4.add_component(de.component.create('Comp3', 'Comp3'))

        lExpected = []
        lExpected.append('Top Level')
        lExpected.append('Top Level.Cca1')
        lExpected.append('Top Level.Cca1.Comp1')
        lExpected.append('Top Level.Cca1.Comp2')
        lExpected.append('Top Level.Cca1.Comp3')
        lExpected.append('Top Level.Cca2')
        lExpected.append('Top Level.Cca2.Comp1')
        lExpected.append('Top Level.Cca2.Comp2')
        lExpected.append('Top Level.Cca2.Comp3')
        lExpected.append('Top Level.Cca3')
        lExpected.append('Top Level.Cca3.Comp1')
        lExpected.append('Top Level.Cca3.Comp2')
        lExpected.append('Top Level.Cca3.Comp3')
        lExpected.append('Top Level.Cca3.Cca4')
        lExpected.append('Top Level.Cca3.Cca4.Comp1')
        lExpected.append('Top Level.Cca3.Cca4.Comp2')
        lExpected.append('Top Level.Cca3.Cca4.Comp3')

        lActual = de.apps.hierarchy.extract(oSystem)
        
        self.assertEqual(lExpected, lActual)

    def test_deep_nested_extract(self):

        oSystem = de.system.create('Top')
        oCca1 = oSystem.add_component(de.hw.cca.create('Cca1'))
        oCca2 = oCca1.add_component(de.hw.cca.create('Cca2'))
        oCca3 = oCca2.add_component(de.hw.cca.create('Cca3'))
        oCca4 = oCca3.add_component(de.hw.cca.create('Cca4'))
        oCca8 = oCca4.add_component(de.hw.cca.create('Cca8'))
        oCca8Comp = oCca8.add_component(de.component.create('Comp2', 'Comp2'))
        oCca5 = oCca4.add_component(de.hw.cca.create('Cca5'))
        oCca6 = oCca5.add_component(de.hw.cca.create('Cca6'))
        oCca7 = oCca6.add_component(de.hw.cca.create('Cca7'))
        oCca7Comp = oCca7.add_component(de.component.create('Comp1', 'Comp1'))

        lExpected = []
        lExpected.append('Top')
        lExpected.append('Top.Cca1')
        lExpected.append('Top.Cca1.Cca2')
        lExpected.append('Top.Cca1.Cca2.Cca3')
        lExpected.append('Top.Cca1.Cca2.Cca3.Cca4')
        lExpected.append('Top.Cca1.Cca2.Cca3.Cca4.Cca8')
        lExpected.append('Top.Cca1.Cca2.Cca3.Cca4.Cca8.Comp2')
        lExpected.append('Top.Cca1.Cca2.Cca3.Cca4.Cca5')
        lExpected.append('Top.Cca1.Cca2.Cca3.Cca4.Cca5.Cca6')
        lExpected.append('Top.Cca1.Cca2.Cca3.Cca4.Cca5.Cca6.Cca7')
        lExpected.append('Top.Cca1.Cca2.Cca3.Cca4.Cca5.Cca6.Cca7.Comp1')

        lActual = de.apps.hierarchy.extract(oSystem)
        
        self.assertEqual(lExpected, lActual)

    def test_deep_nested_update_path(self):

        oSystem = de.system.create('Top')
        oCca1 = oSystem.add_component(de.hw.cca.create('Cca1'))
        oCca2 = oCca1.add_component(de.hw.cca.create('Cca2'))
        oCca3 = oCca2.add_component(de.hw.cca.create('Cca3'))
        oCca4 = oCca3.add_component(de.hw.cca.create('Cca4'))
        oCca8 = oCca4.add_component(de.hw.cca.create('Cca8'))
        oCca8Comp = oCca8.add_component(de.component.create('Comp2', 'Comp2'))
        oCca8CompInterface = oCca8Comp.create_interface('I1')
        oCca5 = oCca4.add_component(de.hw.cca.create('Cca5'))
        oCca6 = oCca5.add_component(de.hw.cca.create('Cca6'))
        oCca7 = oCca6.add_component(de.hw.cca.create('Cca7'))
        oCca7Comp = oCca7.add_component(de.component.create('Comp1', 'Comp1'))
        oCca7CompInterface = oCca7Comp.create_interface('I2')

        de.apps.hierarchy.update_paths(oSystem)

        self.assertEqual(oSystem.path,'Top')
        self.assertEqual(oCca1.path,'Top.Cca1')
        self.assertEqual(oCca2.path,'Top.Cca1.Cca2')
        self.assertEqual(oCca3.path,'Top.Cca1.Cca2.Cca3')
        self.assertEqual(oCca4.path,'Top.Cca1.Cca2.Cca3.Cca4')
        self.assertEqual(oCca5.path,'Top.Cca1.Cca2.Cca3.Cca4.Cca5')
        self.assertEqual(oCca6.path,'Top.Cca1.Cca2.Cca3.Cca4.Cca5.Cca6')
        self.assertEqual(oCca7.path,'Top.Cca1.Cca2.Cca3.Cca4.Cca5.Cca6.Cca7')
        self.assertEqual(oCca8.path,'Top.Cca1.Cca2.Cca3.Cca4.Cca8')
        self.assertEqual(oCca7Comp.path,'Top.Cca1.Cca2.Cca3.Cca4.Cca5.Cca6.Cca7.Comp1')
        self.assertEqual(oCca8Comp.path,'Top.Cca1.Cca2.Cca3.Cca4.Cca8.Comp2')
        self.assertEqual(oCca7CompInterface.path,'Top.Cca1.Cca2.Cca3.Cca4.Cca5.Cca6.Cca7.Comp1.I2')
        self.assertEqual(oCca8CompInterface.path,'Top.Cca1.Cca2.Cca3.Cca4.Cca8.Comp2.I1')


class test_filter_upto_level(unittest.TestCase):

    def setUp(self):
        self.lInput = []
        self.lInput.append('top')
        self.lInput.append('top.1')
        self.lInput.append('top.1.1')
        self.lInput.append('top.1.2')
        self.lInput.append('top.2')
        self.lInput.append('top.2.1')
        self.lInput.append('top.2.2')
        self.lInput.append('top.2.2.1')
        self.lInput.append('top.3')
        self.lInput.append('top.3.1')
        self.lInput.append('top.3.1.1')
        self.lInput.append('top.3.1.2')
        self.lInput.append('top.3.1.2.1')
        self.lInput.append('top.3.2')
        self.lInput.append('top.3.3')
        self.lInput.append('top.4')

    def test_level_1_filter(self):
        lExpected = []
        lExpected.append('top')
        lExpected.append('top.1')
        lExpected.append('top.2')
        lExpected.append('top.3')
        lExpected.append('top.4')

        lActual = de.apps.hierarchy.filter_upto_level(self.lInput, 1)
        self.assertEqual(lExpected, lActual)

    def test_level_2_filter(self):
        lExpected = []
        lExpected.append('top')
        lExpected.append('top.1')
        lExpected.append('top.1.1')
        lExpected.append('top.1.2')
        lExpected.append('top.2')
        lExpected.append('top.2.1')
        lExpected.append('top.2.2')
        lExpected.append('top.3')
        lExpected.append('top.3.1')
        lExpected.append('top.3.2')
        lExpected.append('top.3.3')
        lExpected.append('top.4')

        lActual = de.apps.hierarchy.filter_upto_level(self.lInput, 2)
        self.assertEqual(lExpected, lActual)

    def test_level_3_filter(self):
        lExpected = []

        lExpected.append('top')
        lExpected.append('top.1')
        lExpected.append('top.1.1')
        lExpected.append('top.1.2')
        lExpected.append('top.2')
        lExpected.append('top.2.1')
        lExpected.append('top.2.2')
        lExpected.append('top.2.2.1')
        lExpected.append('top.3')
        lExpected.append('top.3.1')
        lExpected.append('top.3.1.1')
        lExpected.append('top.3.1.2')
        lExpected.append('top.3.2')
        lExpected.append('top.3.3')
        lExpected.append('top.4')

        lActual = de.apps.hierarchy.filter_upto_level(self.lInput, 3)
        self.assertEqual(lExpected, lActual)

    def test_level_4_filter(self):
        lExpected = []

        lExpected.append('top')
        lExpected.append('top.1')
        lExpected.append('top.1.1')
        lExpected.append('top.1.2')
        lExpected.append('top.2')
        lExpected.append('top.2.1')
        lExpected.append('top.2.2')
        lExpected.append('top.2.2.1')
        lExpected.append('top.3')
        lExpected.append('top.3.1')
        lExpected.append('top.3.1.1')
        lExpected.append('top.3.1.2')
        lExpected.append('top.3.1.2.1')
        lExpected.append('top.3.2')
        lExpected.append('top.3.3')
        lExpected.append('top.4')

        lActual = de.apps.hierarchy.filter_upto_level(self.lInput, 4)
        self.assertEqual(lExpected, lActual)

class test_extract_end_points(unittest.TestCase):

    def setUp(self):
        self.lInput = []
        self.lInput.append('top')
        self.lInput.append('top.1')
        self.lInput.append('top.1.1')
        self.lInput.append('top.1.2')
        self.lInput.append('top.2')
        self.lInput.append('top.2.1')
        self.lInput.append('top.2.2')
        self.lInput.append('top.2.2.1')
        self.lInput.append('top.3')
        self.lInput.append('top.3.1')
        self.lInput.append('top.3.1.1')
        self.lInput.append('top.3.1.2')
        self.lInput.append('top.3.1.2.1')
        self.lInput.append('top.3.2')
        self.lInput.append('top.3.3')
        self.lInput.append('top.4')

    def test_extract_end_points(self):
        lExpected = []

        lExpected.append('top.1.1')
        lExpected.append('top.1.2')
        lExpected.append('top.2.1')
        lExpected.append('top.2.2.1')
        lExpected.append('top.3.1.1')
        lExpected.append('top.3.1.2.1')
        lExpected.append('top.3.2')
        lExpected.append('top.3.3')
        lExpected.append('top.4')

        lActual = de.apps.hierarchy.extract_end_points(self.lInput)
        self.assertEqual(lExpected, lActual)

class test_extract_mid_points(unittest.TestCase):

    def setUp(self):
        self.lInput = []
        self.lInput.append('top')
        self.lInput.append('top.1')
        self.lInput.append('top.1.1')
        self.lInput.append('top.1.2')
        self.lInput.append('top.2')
        self.lInput.append('top.2.1')
        self.lInput.append('top.2.2')
        self.lInput.append('top.2.2.1')
        self.lInput.append('top.3')
        self.lInput.append('top.3.1')
        self.lInput.append('top.3.1.1')
        self.lInput.append('top.3.1.2')
        self.lInput.append('top.3.1.2.1')
        self.lInput.append('top.3.2')
        self.lInput.append('top.3.3')
        self.lInput.append('top.4')

    def test_extract_mid_points(self):
        lExpected = []

        lExpected.append('top')
        lExpected.append('top.1')
        lExpected.append('top.2')
        lExpected.append('top.2.2')
        lExpected.append('top.3')
        lExpected.append('top.3.1')
        lExpected.append('top.3.1.2')

        lActual = de.apps.hierarchy.extract_mid_points(self.lInput)
        self.assertEqual(lExpected, lActual)

if __name__ == '__main__':
    unittest.main()
