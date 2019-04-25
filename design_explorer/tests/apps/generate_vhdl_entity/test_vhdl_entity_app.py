

import unittest
import design_explorer as de

class test_system(unittest.TestCase):


    def test_entity_wo_interfaces(self):
        oHdlComponent = de.hdl.component.create('hdl_top')

        lExpected = []
        lExpected.append('entity HDL_TOP is')
        lExpected.append('  port (')
        lExpected.append('  );')
        lExpected.append('end entity HDL_TOP;')

        self.assertEqual(lExpected, de.apps.generate_vhdl_entity(oHdlComponent))

    def test_entity_with_interfaces_wo_ports(self):
        oHdlComponent = de.hdl.component.create('hdl_top')
        oInterface1 = oHdlComponent.create_interface('Interface1')
        oInterface2 = oHdlComponent.create_interface('Interface2')

        lExpected = []
        lExpected.append('entity HDL_TOP is')
        lExpected.append('  port (')
        lExpected.append('    -- [I:Interface1]')
        lExpected.append('')
        lExpected.append('    -- [I:Interface2]')
        lExpected.append('  );')
        lExpected.append('end entity HDL_TOP;')

        self.assertEqual(lExpected, de.apps.generate_vhdl_entity(oHdlComponent))
         
    def test_entity_with_interfaces_with_single_bit_ports(self):
        oHdlComponent = de.hdl.component.create('hdl_top')
        oInterface1 = oHdlComponent.create_interface('Interface1')
        oInterface2 = oHdlComponent.create_interface('Interface2')
        oInterface1.create_port('I1_PORT1', 1, False, 'Port 1 of interface 1')
        oInterface1.create_port('I1_PORT2', 1, True, 'Port 2 of interface 1')

        oInterface2.create_port('I2_PORT1', 1, True, 'Port 1 of interface 2')
        oInterface2.create_port('I2_PORT2', 1, False, 'Port 2 of interface 2')

        lExpected = []
        lExpected.append('entity HDL_TOP is')
        lExpected.append('  port (')
        lExpected.append('    -- [I:Interface1]')
        lExpected.append('    I1_PORT1 : in std_logic; -- Port 1 of interface 1')
        lExpected.append('    I1_PORT2 : out std_logic; -- Port 2 of interface 1')
        lExpected.append('')
        lExpected.append('    -- [I:Interface2]')
        lExpected.append('    I2_PORT1 : out std_logic; -- Port 1 of interface 2')
        lExpected.append('    I2_PORT2 : in std_logic; -- Port 2 of interface 2')
        lExpected.append('  );')
        lExpected.append('end entity HDL_TOP;')

        self.assertEqual(lExpected, de.apps.generate_vhdl_entity(oHdlComponent))

    def test_entity_with_interfaces_with_multiple_bit_ports(self):
        oHdlComponent = de.hdl.component.create('hdl_top')
        oInterface1 = oHdlComponent.create_interface('Interface1')
        oInterface2 = oHdlComponent.create_interface('Interface2')
        oInterface1.create_port('I1_PORT1', 9, False, 'Port 1 of interface 1')
        oInterface1.create_port('I1_PORT2', 1, True, 'Port 2 of interface 1')

        oInterface2.create_port('I2_PORT1', 1, True, 'Port 1 of interface 2')
        oInterface2.create_port('I2_PORT2', 32, False, 'Port 2 of interface 2')

        lExpected = []
        lExpected.append('entity HDL_TOP is')
        lExpected.append('  port (')
        lExpected.append('    -- [I:Interface1]')
        lExpected.append('    I1_PORT1 : in std_logic_vector(8 downto 0); -- Port 1 of interface 1')
        lExpected.append('    I1_PORT2 : out std_logic; -- Port 2 of interface 1')
        lExpected.append('')
        lExpected.append('    -- [I:Interface2]')
        lExpected.append('    I2_PORT1 : out std_logic; -- Port 1 of interface 2')
        lExpected.append('    I2_PORT2 : in std_logic_vector(31 downto 0); -- Port 2 of interface 2')
        lExpected.append('  );')
        lExpected.append('end entity HDL_TOP;')

        self.assertEqual(lExpected, de.apps.generate_vhdl_entity(oHdlComponent))

    def test_entity_with_interfaces_with_ports_without_descriptions(self):
        oHdlComponent = de.hdl.component.create('hdl_top')
        oInterface1 = oHdlComponent.create_interface('Interface1')
        oInterface2 = oHdlComponent.create_interface('Interface2')
        oInterface1.create_port('I1_PORT1', 9, False, 'Port 1 of interface 1')
        oInterface1.create_port('I1_PORT2', 1, True)

        oInterface2.create_port('I2_PORT1', 1, True)
        oInterface2.create_port('I2_PORT2', 32, False, 'Port 2 of interface 2')

        lExpected = []
        lExpected.append('entity HDL_TOP is')
        lExpected.append('  port (')
        lExpected.append('    -- [I:Interface1]')
        lExpected.append('    I1_PORT1 : in std_logic_vector(8 downto 0); -- Port 1 of interface 1')
        lExpected.append('    I1_PORT2 : out std_logic; -- ::WARNING:: Missing description')
        lExpected.append('')
        lExpected.append('    -- [I:Interface2]')
        lExpected.append('    I2_PORT1 : out std_logic; -- ::WARNING:: Missing description')
        lExpected.append('    I2_PORT2 : in std_logic_vector(31 downto 0); -- Port 2 of interface 2')
        lExpected.append('  );')
        lExpected.append('end entity HDL_TOP;')

        self.assertEqual(lExpected, de.apps.generate_vhdl_entity(oHdlComponent))
if __name__ == '__main__':
    unittest.main()
