
import unittest
from design_explorer import port
from design_explorer import interface


class test_interface(unittest.TestCase):

    def test_interface_class_attributes_exist(self):
        oInterface = interface.create('Interface1')
        self.assertEqual(oInterface.name, 'Interface1')
        self.assertEqual(oInterface.ports, None)
        self.assertEqual(oInterface.source, False)

    def test_interface_add_port_method(self):
        oInterface = interface.create('Interface1')
        oInterface.add_port(port.create('Port1', 10, 'out', 'This is port 1'))
        oInterface.add_port(port.create('Port2', 5, 'in', 'This is port 2'))

        self.assertEqual(len(oInterface.ports), 2)
        self.assertEqual(oInterface.ports[0].name, 'Port1')
        self.assertEqual(oInterface.ports[1].name, 'Port2')

    def test_interface_create_port_method(self):
        oInterface = interface.create('Interface1')

        oPort1 = oInterface.create_port('Port1', 10, 'out', 'This is port 1')
        oPort2 = oInterface.create_port('Port2', 5, 'in', 'This is port 2')

        self.assertEqual(len(oInterface.ports), 2)
        self.assertEqual(oInterface.ports[0].name, 'Port1')
        self.assertEqual(oInterface.ports[1].name, 'Port2')

        self.assertEqual(oPort1.name, 'Port1')
        self.assertEqual(oPort2.name, 'Port2')
        self.assertEqual(oPort1.description, 'This is port 1')
        self.assertEqual(oInterface.ports[0].description, 'This is port 1')

        oPort1.description = 'New port 1 description'

        self.assertEqual(oPort1.description, 'New port 1 description')
        self.assertEqual(oInterface.ports[0].description, 'New port 1 description')

    def test_get_number_ports_method(self):
        oInterface = interface.create('Interface1')

        
        self.assertEqual(oInterface.get_number_ports(), 0)

        oInterface.add_port(port.create('Port1', 10, 'out', 'This is port 1'))
        oInterface.add_port(port.create('Port2', 5, 'in', 'This is port 2'))

        self.assertEqual(oInterface.get_number_ports(), 15)

        oInterface.add_port(port.create('Port3', 3, 'in', 'This is port 3'))

        self.assertEqual(oInterface.get_number_ports(), 18)

if __name__ == '__main__':
    unittest.main()
