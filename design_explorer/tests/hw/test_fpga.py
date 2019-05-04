
import unittest
from design_explorer.hw import fpga
#from design_explorer.hw import port
#from design_explorer.hw import interface


class test_hw_fpga(unittest.TestCase):

    def test_fpga_class_attributes_exist(self):
        oFpga = fpga.create('fpga')
        self.assertEqual(oFpga.name, 'fpga')
        self.assertEqual(oFpga.instanceName, None)
        self.assertEqual(oFpga.hdl_blocks, None)
        self.assertEqual(oFpga.type, 'fpga')

    def test_fpga_add_hdl_block_method(self):
        oFpga = fpga.create('fpga1')
        oFpga.add_hdl_block('Block1')
        oFpga.add_hdl_block('Block2')
        oFpga.add_hdl_block('Block3')
        self.assertEqual(len(oFpga.hdl_blocks), 3)
        self.assertEqual(oFpga.hdl_blocks[0], 'Block1')
        self.assertEqual(oFpga.hdl_blocks[1], 'Block2')
        self.assertEqual(oFpga.hdl_blocks[2], 'Block3')

if __name__ == '__main__':
    unittest.main()
