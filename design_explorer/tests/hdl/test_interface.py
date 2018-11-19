
import unittest
from design_explorer.hdl import port
from design_explorer.hdl import interface


class test_hdl_interface(unittest.TestCase):

    def test_interface_class_attributes_exist(self):
        oInterface = interface.create('Interface1')
        self.assertEqual(oInterface.name, 'Interface1')
        self.assertEqual(oInterface.description, None)
        self.assertEqual(oInterface.ports, None)
        self.assertEqual(oInterface.port_types, None)

    def test_interface_add_source_and_sink_port_methods(self):
        oPort1 = port.create('Port1')
        oPort2 = port.create('Port2')
        oPort3 = port.create('Port3')
        oPort4 = port.create('Port4')
        oInterface = interface.create('Interface1')
        oInterface.add_source_port(oPort1)
        oInterface.add_sink_port(oPort2)
        oInterface.add_source_port(oPort3)
        oInterface.add_sink_port(oPort4)
        self.assertEqual(len(oInterface.ports),4)
        self.assertEqual(len(oInterface.port_types),4)
        self.assertEqual(oInterface.ports[0].name, 'Port1')
        self.assertEqual(oInterface.port_types[0], 'Source')
        self.assertEqual(oInterface.ports[1].name, 'Port2')
        self.assertEqual(oInterface.port_types[1], 'Sink')
        self.assertEqual(oInterface.ports[2].name, 'Port3')
        self.assertEqual(oInterface.port_types[2], 'Source')
        self.assertEqual(oInterface.ports[3].name, 'Port4')
        self.assertEqual(oInterface.port_types[3], 'Sink')

    def test_interface_extract_port_list_wo_ports_method(self):
        oInterface = interface.create('Interface1')
        lExpected = []
        lExpected.append('-- [I:Interface1]')
        self.assertEqual(oInterface.extract_port_list('Source'), lExpected)

    def test_interface_port_map_w_ports_method(self):
        oInterface = interface.create('Interface1')
        oPort1 = port.create('Port1')
        oPort2 = port.create('Port2')
        oPort3 = port.create('Port3')
        oPort4 = port.create('Port4')
        oInterface.add_source_port(oPort1)
        oInterface.add_sink_port(oPort2)
        oInterface.add_source_port(oPort3)
        oInterface.add_sink_port(oPort4)
        lExpected = []
        lExpected.append('-- [I:Interface1]')
        lExpected.append('Port1 : out')
        lExpected.append('Port2 : in')
        lExpected.append('Port3 : out')
        lExpected.append('Port4 : in')
        self.assertEqual(oInterface.extract_port_list('Source'), lExpected)
        lExpected = []
        lExpected.append('-- [I:Interface1]')
        lExpected.append('Port1 : in')
        lExpected.append('Port2 : out')
        lExpected.append('Port3 : in')
        lExpected.append('Port4 : out')
        self.assertEqual(oInterface.extract_port_list('Sink'), lExpected)
 

if __name__ == '__main__':
    unittest.main()
