
import unittest
from design_explorer import connect
from design_explorer.hdl import subblock
from design_explorer import interface


class test_connect(unittest.TestCase):

    def test_connect_class_attributes_exist(self):
        oSubblock1 = subblock.create('Subblock1')
        oInterface1 = interface.create('Interface1')
        oSubblock1.add_source_interface(oInterface1)

        oSubblock2 = subblock.create('Subblock2')
        oInterface2 = interface.create('Interface2')
        oSubblock2.add_sink_interface(oInterface2)

        oConnection = connect.create('Connection1')
        oConnection.add_source(oSubblock1, 'Interface1')
        oConnection.add_sink(oSubblock2, 'Interface2')
        self.assertEqual(oConnection.name, 'Connection1')
        self.assertEqual(oConnection.source.name, 'Subblock1')
        self.assertEqual(oConnection.source_interface.name, 'Interface1')
        self.assertEqual(oConnection.sink.name, 'Subblock2')
        self.assertEqual(oConnection.sink_interface.name, 'Interface2')

if __name__ == '__main__':
    unittest.main()
