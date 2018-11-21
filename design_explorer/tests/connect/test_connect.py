
import unittest
from design_explorer import connect
from design_explorer.hdl import interface


class test_connect(unittest.TestCase):

    def test_connect_class_attributes_exist(self):
        oInterface1 = interface.create('Interface1')
        oInterface2 = interface.create('Interface2')
        oConnection = connect.create('Connection1', oInterface1, oInterface2)
        self.assertEqual(oConnection.name, 'Connection1')
        self.assertEqual(oConnection.source.name, 'Interface1')
        self.assertEqual(oConnection.sink.name, 'Interface2')

if __name__ == '__main__':
    unittest.main()
