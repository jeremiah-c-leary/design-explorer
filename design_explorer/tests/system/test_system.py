
import unittest
from design_explorer import system
from design_explorer import hw
from design_explorer import connection
from design_explorer import component
from design_explorer.hdl import subblock
from design_explorer import interface


class test_system(unittest.TestCase):

    def test_system_class_attributes_exist(self):
        oSystem = system.create('instance')
        self.assertEqual(oSystem.name, 'instance')
        self.assertEqual(oSystem.components, None)
        self.assertEqual(oSystem.connections, None)

    def test_system_add_component_method(self):
        oSystem = system.create('System1')
        oSystem.add_component(component.create('Component1'))
        oSystem.add_component(component.create('Component2'))
        oSystem.add_component(component.create('Component3'))

        self.assertEqual(len(oSystem.components), 3)
        self.assertEqual(oSystem.components[0].name, 'Component1')
        self.assertEqual(oSystem.components[1].name, 'Component2')
        self.assertEqual(oSystem.components[2].name, 'Component3')

    def test_system_add_connection_method(self):
        oSystem = system.create('System1')

        oSubblock1 = subblock.create('Subblock1')
        oSubblock1.create_interface('Interface1.0')
        oSubblock1.create_interface('Interface1.1')
        oSystem.add_component(oSubblock1)

        oSubblock2 = subblock.create('Subblock2')
        oSubblock2.create_interface('Interface2.0')
        oSubblock2.create_interface('Interface2.1')
        oSystem.add_component(oSubblock2)

        oSubblock3 = subblock.create('Subblock3')
        oSubblock3.create_interface('Interface3.0')
        oSubblock3.create_interface('Interface3.1')
        oSystem.add_component(oSubblock3)

        oConnection1 = connection.create('con1', oSubblock1.get_interface_named('Interface1.0'), oSubblock2.get_interface_named('Interface2.0'))
        oConnection2 = connection.create('con2', oSubblock1.get_interface_named('Interface1.0'), oSubblock3.get_interface_named('Interface3.0'))
        oConnection3 = connection.create('con3', oSubblock1.get_interface_named('Interface1.1'), oSubblock2.get_interface_named('Interface3.1'))
        oConnection4 = connection.create('con4', oSubblock2.get_interface_named('Interface2.1'), oSubblock2.get_interface_named('Interface1.1'))

        oSystem.add_connection(oConnection1)
        oSystem.add_connection(oConnection2)
        oSystem.add_connection(oConnection3)
        oSystem.add_connection(oConnection3)

        self.assertEqual(len(oSystem.connections), 4)
        self.assertEqual(oSystem.connections[0].source.name, 'Interface1.0')
        self.assertEqual(oSystem.connections[1].source.name, 'Interface1.0')

if __name__ == '__main__':
    unittest.main()
