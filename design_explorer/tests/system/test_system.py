
import unittest
from design_explorer.system import system


class test_hdl_system(unittest.TestCase):

    def test_system_class_attributes_exist(self):
        oSystem = system.create('instance')
        self.assertEqual(oSystem.instance_name, 'instance')
        self.assertEqual(oSystem.subblocks, None)

    def test_system_add_subblock_method(self):
        oSystem = system.create('System1')
        oSystem.add_subblock('SubBlock1')
        oSystem.add_subblock('SubBlock2')
        oSystem.add_subblock('SubBlock3')

        self.assertEqual(len(oSystem.subblocks), 3)
        self.assertEqual(oSystem.subblocks[0], 'SubBlock1')
        self.assertEqual(oSystem.subblocks[1], 'SubBlock2')
        self.assertEqual(oSystem.subblocks[2], 'SubBlock3')


if __name__ == '__main__':
    unittest.main()
