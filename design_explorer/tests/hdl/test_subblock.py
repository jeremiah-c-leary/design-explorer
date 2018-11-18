
import unittest
from design_explorer.hdl import subblock


class testHdlSubblock(unittest.TestCase):

    def test_subblock_class_attributes_exist(self):
        oSubblock = subblock.create('instance')
        self.assertEqual(oSubblock.instance_name, 'instance')
        self.assertEqual(oSubblock.source_interfaces, None)
        self.assertEqual(oSubblock.sink_interfaces, None)

if __name__ == '__main__':
    unittest.main()
