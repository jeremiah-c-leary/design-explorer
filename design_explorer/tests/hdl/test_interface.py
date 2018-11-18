
import unittest
from design_explorer.hdl import port
from design_explorer.hdl import interface


class test_hdl_interface(unittest.TestCase):

    def test_interface_class_attributes_exist(self):
        oInterface = interface.create('Interface1')
        self.assertEqual(oInterface.name, 'Interface1')
        self.assertEqual(oInterface.description, None)
        self.assertEqual(oInterface.source_ports, None)
        self.assertEqual(oInterface.sink_ports, None)

    def test_interface_add_source_port_method(self):
        oPort1 = port.create('Port1')
        oPort2 = port.create('Port2')
        oPort3 = port.create('Port3')
        oPort4 = port.create('Port4')
        oInterface = interface.create('Interface1')
        oInterface.add_source_port(oPort1)
        oInterface.add_source_port(oPort2)
        self.assertEqual(len(oInterface.source_ports),2)
        self.assertEqual(oInterface.source_ports[0].name, 'Port1')
        self.assertEqual(oInterface.source_ports[1].name, 'Port2')

    def test_interface_add_sink_port_method(self):
        oPort1 = port.create('Port1')
        oPort2 = port.create('Port2')
        oPort3 = port.create('Port3')
        oPort4 = port.create('Port4')
        oInterface = interface.create('Interface1')
        oInterface.add_sink_port(oPort1)
        oInterface.add_sink_port(oPort2)
        self.assertEqual(len(oInterface.sink_ports),2)
        self.assertEqual(oInterface.sink_ports[0].name, 'Port1')
        self.assertEqual(oInterface.sink_ports[1].name, 'Port2')

if __name__ == '__main__':
    unittest.main()
