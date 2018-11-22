
import unittest
from design_explorer import system
from design_explorer import hw
from design_explorer import connect
from design_explorer.hdl import subblock
from design_explorer.hdl import interface


class test_system(unittest.TestCase):

    def test_system_class_attributes_exist(self):
        oSystem = system.create('instance')
        self.assertEqual(oSystem.name, 'instance')
        self.assertEqual(oSystem.components, None)
        self.assertEqual(oSystem.connections, None)

    def test_system_add_component_method(self):
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

    def test_system_add_connection_method(self):
        oSystem = system.create('System1')

        oSubblock1 = subblock.create('Subblock1')
        oInterface1 = interface.create('Interface1.0')
        oSubblock1.add_source_interface(oInterface1)
        oInterface1 = interface.create('Interface1.1')
        oSubblock1.add_source_interface(oInterface1)
        oSystem.add_component(oSubblock1)

        oSubblock2 = subblock.create('Subblock2')
        oInterface2 = interface.create('Interface2')
        oSubblock2.add_sink_interface(oInterface2)
        oSystem.add_component(oSubblock2)

        oSubblock3 = subblock.create('Subblock3')
        oInterface3 = interface.create('Interface3')
        oSubblock3.add_sink_interface(oInterface3)
        oSystem.add_component(oSubblock3)

        oConnection1 = connect.create('Connection1', oSubblock1, 'Interface1.0', oSubblock2, 'Interface2')
        oConnection2 = connect.create('Connection2', oSubblock1, 'Interface1.1', oSubblock3, 'Interface3')

        oSystem.add_connection(oConnection1)
        oSystem.add_connection(oConnection2)

        self.assertEqual(len(oSystem.connections), 2)
        self.assertEqual(oSystem.connections[0].source_interface.name, 'Interface1.0')
        self.assertEqual(oSystem.connections[1].source_interface.name, 'Interface1.1')

if __name__ == '__main__':
    unittest.main()
