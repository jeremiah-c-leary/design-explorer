
import unittest
import design_explorer as de


class test_connection(unittest.TestCase):

    def test_connection_class_attributes_exist(self):
        oSystem = de.system.create('Top Level')
        oComponent1 = oSystem.add_component(de.component.create('Component1', 'Component1'))
        oInterface1 = oComponent1.create_interface('Interface1')
        oInterface1.create_port('I1 P1', 1, 'out')
        oInterface1.create_port('I1 P2', 1, 'out')
        oInterface1.create_port('I1 P3', 1, 'out')
        oInterface1.create_port('I1 P4', 1, 'out')

        oComponent2 = oSystem.add_component(de.component.create('Component2', 'Component2'))
        oInterface2 = oComponent2.create_interface('Interface2')
        oInterface2.create_port('I2 P1', 1, 'out')
        oInterface2.create_port('I2 P2', 1, 'out')
        oInterface2.create_port('I2 P3', 1, 'out')
        oInterface2.create_port('I2 P4', 1, 'out')

        oConnection = de.connection.create('con1', oSystem, 'Component1.Interface1', 'Component2.Interface2')

        self.assertEqual(oConnection.name, 'con1')
        self.assertEqual(oConnection.source.name, 'Interface1')
        self.assertEqual(oConnection.sink.name, 'Interface2')

        dMap = {}
        dMap['I1 P1'] = 'I2 P1'
        dMap['I1 P2'] = 'I2 P2'
        dMap['I1 P3'] = 'I2 P3'
        dMap['I1 P4'] = 'I2 P4'

        self.assertEqual(dMap, oConnection.map)

    def test_connection_map_port_method(self):
        oSystem = de.system.create('Top Level')
        oComponent1 = oSystem.add_component(de.component.create('Component1', 'Component1'))
        oInterface1 = oComponent1.create_interface('Interface1')
        oInterface1.create_port('I1 P1', 1, 'out')
        oInterface1.create_port('I1 P2', 1, 'out')
        oInterface1.create_port('I1 P3', 1, 'out')
        oInterface1.create_port('I1 P4', 1, 'out')

        oComponent2 = oSystem.add_component(de.component.create('Component2', 'Component2'))
        oInterface2 = oComponent2.create_interface('Interface2')
        oInterface2.create_port('I2 P1', 1, 'out')
        oInterface2.create_port('I2 P2', 1, 'out')
        oInterface2.create_port('I2 P3', 1, 'out')
        oInterface2.create_port('I2 P4', 1, 'out')

        oConnection = de.connection.create('con1', oSystem, 'Component1.Interface1', 'Component2.Interface2', False)

        self.assertEqual(None, oConnection.map)

        oConnection.map_port('I1 P1', 'I2 P4')

        dMap = {}
        dMap['I1 P1'] = 'I2 P4'

        self.assertEqual(dMap, oConnection.map)

    def test_multilevel_connection(self):
        oSystem = de.system.create('top')
        oCca1 = de.hw.cca.create('Cca1')
        oCca2 = de.hw.cca.create('Cca2')
        oCca3 = de.hw.cca.create('Cca3')
        oCca4 = de.hw.cca.create('Cca4')
        oCca5 = de.hw.cca.create('Cca5')
        oCca6 = de.hw.cca.create('Cca6')

        oSystem.add_component(oCca1)
        oSystem.add_component(oCca2)
        oCca1.add_component(oCca3)
        oCca2.add_component(oCca4)
        oCca3.add_component(oCca5)
        oCca4.add_component(oCca6)

        oCca5Comp1 = oCca5.add_component(de.component.create('Cca5Comp1', 'Cca5Comp1'))
        oInterface1 = oCca5Comp1.create_interface('I1')
        oCca6Comp2 = oCca6.add_component(de.component.create('Cca6Comp1', 'Cca6Comp1'))
        oInterface2 = oCca6Comp2.create_interface('I2')


        oCon1 = de.connection.create('con1', oSystem, 'Cca1.Cca3.Cca5.Cca5Comp1.I1', 'Cca2.Cca4.Cca6.Cca6Comp1.I2', False)

        self.assertEqual(oInterface1, oCon1.source)
        self.assertEqual(oInterface2, oCon1.sink)


if __name__ == '__main__':
    unittest.main()
