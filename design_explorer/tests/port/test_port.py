
import unittest
from design_explorer import port


class test_port(unittest.TestCase):

    def test_port_class_attributes_exist(self):
        oPort = port.create('portName')
        self.assertEqual(oPort.name, 'portName')
        self.assertEqual(oPort.width, None)
        self.assertEqual(oPort.source, False)
        self.assertEqual(oPort.description, None)

    def test_creating_port(self):
        oPort = port.create('Port1', 10, True, 'This is a port')
        self.assertEqual(oPort.name, 'Port1')
        self.assertEqual(oPort.width, 10)
        self.assertEqual(oPort.source, True)
        self.assertEqual(oPort.description, 'This is a port')

if __name__ == '__main__':
    unittest.main()
