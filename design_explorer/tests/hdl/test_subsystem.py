
import unittest
from design_explorer.hdl import subsystem
from design_explorer.hdl import subblock


class testHdlSubsystem(unittest.TestCase):

    def test_subsystem_class_attributes_exist(self):
        oSubsystem = subsystem.create('instance')
        self.assertEqual(oSubsystem.instance_name, 'instance')
        self.assertEqual(oSubsystem.subblocks, None)

    def test_subsystem_add_subblock_method(self):
        oSub1 = subblock.create('Sub1')
        oSub2 = subblock.create('Sub2')
        oSub3 = subblock.create('Sub3')

        oSystem = subsystem.create('Subsystem1')
        oSystem.add_subblock(oSub1)
        oSystem.add_subblock(oSub2)
        oSystem.add_subblock(oSub3)

        self.assertEqual(len(oSystem.subblocks), 3)
        self.assertEqual(oSystem.subblocks[0].instance_name, 'Sub1')
        self.assertEqual(oSystem.subblocks[1].instance_name, 'Sub2')
        self.assertEqual(oSystem.subblocks[2].instance_name, 'Sub3')



if __name__ == '__main__':
    unittest.main()
