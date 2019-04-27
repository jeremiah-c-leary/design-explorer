
import unittest
from design_explorer import port


class test_port(unittest.TestCase):

    def test_port_class_attributes_exist(self):
        oPort = port.create('portName')
        self.assertEqual(oPort.name, 'portName')
        self.assertEqual(oPort.width, None)
        self.assertEqual(oPort.direction, 'in')
        self.assertEqual(oPort.description, None)

    def test_creating_out_port(self):
        oPort = port.create('Port1', 10, 'out', 'This is an out port')
        self.assertEqual(oPort.name, 'Port1')
        self.assertEqual(oPort.width, 10)
        self.assertEqual(oPort.direction, 'out')
        self.assertEqual(oPort.description, 'This is an out port')

    def test_creating_in_port(self):
        oPort = port.create('Port1', 10, 'in', 'This is an in port')
        self.assertEqual(oPort.name, 'Port1')
        self.assertEqual(oPort.width, 10)
        self.assertEqual(oPort.direction, 'in')
        self.assertEqual(oPort.description, 'This is an in port')

    def test_creating_inout_port(self):
        oPort = port.create('Port1', 10, 'inout', 'This is an inout port')
        self.assertEqual(oPort.name, 'Port1')
        self.assertEqual(oPort.width, 10)
        self.assertEqual(oPort.direction, 'inout')
        self.assertEqual(oPort.description, 'This is an inout port')

    def test_invalid_port_direction(self):
        self.assertRaises(ValueError, port.create, 'Port1', 10, 'bidir', 'This is an inout port')

if __name__ == '__main__':
    unittest.main()
