
import unittest
from design_explorer import system
from design_explorer import hw


class test_system(unittest.TestCase):

    def test_system_class_attributes_exist(self):
        oSystem = system.create('instance')
        self.assertEqual(oSystem.name, 'instance')
        self.assertEqual(oSystem.components, None)

    def test_system_add_subblock_method(self):
        oSystem = system.create('System1')
        oSystem.add_component('SubBlock1')
        oSystem.add_component('SubBlock2')
        oSystem.add_component('SubBlock3')

        self.assertEqual(len(oSystem.components), 3)
        self.assertEqual(oSystem.components[0], 'SubBlock1')
        self.assertEqual(oSystem.components[1], 'SubBlock2')
        self.assertEqual(oSystem.components[2], 'SubBlock3')

    def test_system_extract_node_list_method(self):
        oSystem = system.create('System1')
        oSystem.add_component(hw.fpga.create('FPGA1'))
        oSystem.add_component(hw.component.create('DAC_1'))
        oSystem.add_component(hw.component.create('DAC_2'))
        oSystem.add_component(hw.component.create('ADC'))
        oSystem.add_component(hw.component.create('MEMORY'))
        lExpected = []
        lExpected.append('Id,Label')
        lExpected.append('1,FPGA1')
        lExpected.append('2,DAC_1')
        lExpected.append('3,DAC_2')
        lExpected.append('4,ADC')
        lExpected.append('5,MEMORY')
        self.assertEqual(oSystem.extract_node_list(), lExpected)


if __name__ == '__main__':
    unittest.main()
