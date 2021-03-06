
import unittest
from design_explorer import system
from design_explorer import connection
from design_explorer import component
from design_explorer.hdl import subblock
import design_explorer as de


class test_system(unittest.TestCase):

    def test_system_class_attributes_exist(self):
        oSystem = system.create('instance')
        self.assertEqual(oSystem.name, 'instance')
        self.assertEqual(oSystem.components, None)
        self.assertEqual(oSystem.connections, None)
        self.assertEqual(oSystem.type, 'system')

    def test_system_add_component_method(self):
        oSystem = system.create('System1')
        oSystem.add_component(component.create('Component1', 'Component1'))
        oSystem.add_component(component.create('Component2', 'Component2'))
        oComponent3 = oSystem.add_component(component.create('Component3', 'Component3'))

        self.assertEqual(len(oSystem.components), 3)
        self.assertEqual(oSystem.components[0].name, 'Component1')
        self.assertEqual(oSystem.components[1].name, 'Component2')
        self.assertEqual(oSystem.components[2].name, 'Component3')
        self.assertEqual(oComponent3, oSystem.components[2])

    def test_system_add_connection_method(self):
        oSystem = system.create('System1')

        oSubblock1 = oSystem.add_component(subblock.create('Subblock1', 'Subblock1'))
        oSubblock1.create_interface('Interface1_0')
        oSubblock1.create_interface('Interface1_1')

        oSubblock2 = oSystem.add_component(subblock.create('Subblock2', 'Subblock2'))
        oSubblock2.create_interface('Interface2_0')
        oSubblock2.create_interface('Interface2_1')

        oSubblock3 = oSystem.add_component(subblock.create('Subblock3', 'Subblock3'))
        oSubblock3.create_interface('Interface3_0')
        oSubblock3.create_interface('Interface3_1')

        oConnection1 = connection.create('con1', oSystem, 'Subblock1.Interface1_0', 'Subblock2.Interface2_0', False)
        oConnection2 = connection.create('con2', oSystem, 'Subblock1.Interface1_0', 'Subblock3.Interface3_0', False)
        oConnection3 = connection.create('con3', oSystem, 'Subblock1.Interface1_1', 'Subblock3.Interface3_1', False)
        oConnection4 = connection.create('con4', oSystem, 'Subblock2.Interface2_1', 'Subblock1.Interface1_1', False)

        oSystem.add_connection(oConnection1)
        oSystem.add_connection(oConnection2)
        oSystem.add_connection(oConnection3)
        oSystem.add_connection(oConnection4)

        self.assertEqual(len(oSystem.connections), 4)
        self.assertEqual(oSystem.connections[0].source.name, 'Interface1_0')
        self.assertEqual(oSystem.connections[1].source.name, 'Interface1_0')
        self.assertEqual(oSystem.connections[2].source.name, 'Interface1_1')
        self.assertEqual(oSystem.connections[3].source.name, 'Interface2_1')

    def test_get_component_named_method(self):
        oSystem = system.create('System1')
        oCca = oSystem.add_component(de.hw.cca.create('CCA'))
        oCca2 = oCca.add_component(de.hw.cca.create('CCA2'))
        oComponent1 = oCca.add_component(component.create('Component1', 'Component1'))
        oComponent2 = oCca.add_component(component.create('Component2', 'Component2'))
        oComponent3 = oCca.add_component(component.create('Component3', 'Component3'))
        oComponent4 = oCca2.add_component(component.create('Component4', 'Component4'))

        self.assertEqual(oCca.get_component_named('Component1'), oComponent1)
        self.assertEqual(oCca.get_component_named('Component2'), oComponent2)
        self.assertEqual(oCca.get_component_named('Component3'), oComponent3)
        self.assertRaises(ValueError, oCca.get_component_named,'Comp1')

        self.assertEqual(oSystem.get_component_named('CCA.Component1'), oComponent1)
        self.assertEqual(oSystem.get_component_named('CCA.Component2'), oComponent2)
        self.assertEqual(oSystem.get_component_named('CCA.Component3'), oComponent3)
        self.assertEqual(oSystem.get_component_named('CCA.CCA2.Component4'), oComponent4)
        self.assertRaises(ValueError, oSystem.get_component_named,'CCA.CCA2.Component5')
        self.assertRaises(ValueError, oSystem.get_component_named,'CCA.Component5')


if __name__ == '__main__':
    unittest.main()
