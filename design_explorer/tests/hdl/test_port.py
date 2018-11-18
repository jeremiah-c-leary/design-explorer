
import unittest
from design_explorer.hdl import port


class test_hdl_port(unittest.TestCase):

    def test_port_class_attributes_exist(self):
        oPort = port.create('portName')
        self.assertEqual(oPort.name, 'portName')
        self.assertEqual(oPort.width, None)
        self.assertEqual(oPort.description, None)

if __name__ == '__main__':
    unittest.main()
