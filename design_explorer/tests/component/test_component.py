
import unittest
from design_explorer import component
from design_explorer import port
from design_explorer import interface


class test_hw_component(unittest.TestCase):

    def test_component_class_attributes_exist(self):
        oComponent = component.create('component1')
        self.assertEqual(oComponent.name, 'component1')
        self.assertEqual(oComponent.interfaces, None)
        self.assertEqual(oComponent.interface_types, None)

    def test_component_add_sink_and_source_interface_methods(self):
        oPort1 = port.create('Port1')
        oPort2 = port.create('Port2')
        oPort3 = port.create('Port3')
        oPort4 = port.create('Port4')
        oIntSource = interface.create('Interface1')
        oIntSource.add_source_port(oPort1)
        oIntSource.add_sink_port(oPort2)
        oIntSink = interface.create('Interface2')
        oIntSink.add_source_port(oPort3)
        oIntSink.add_sink_port(oPort4)
        oComponent = component.create('component')
        oComponent.add_source_interface(oIntSource)
        oComponent.add_sink_interface(oIntSink)
        self.assertEqual(oComponent.interfaces[0].name, 'Interface1')
        self.assertEqual(oComponent.interfaces[0].ports[0].name, 'Port1')
        self.assertEqual(oComponent.interfaces[0].ports[1].name, 'Port2')

        self.assertEqual(oComponent.interfaces[1].name, 'Interface2')
        self.assertEqual(oComponent.interfaces[1].ports[0].name, 'Port3')
        self.assertEqual(oComponent.interfaces[1].ports[1].name, 'Port4')

    def test_component_add_sink_and_source_interface_w_renaming_methods(self):
        oPort1 = port.create('Port1')
        oPort2 = port.create('Port2')
        oPort3 = port.create('Port3')
        oPort4 = port.create('Port4')
        oIntSource = interface.create('Interface1')
        oIntSource.add_source_port(oPort1)
        oIntSource.add_sink_port(oPort2)
        oIntSink = interface.create('Interface2')
        oIntSink.add_source_port(oPort3)
        oIntSink.add_sink_port(oPort4)
        oComponent = component.create('component')
        oComponent.add_source_interface(oIntSource, 'source_interface')
        oComponent.add_sink_interface(oIntSink, 'sink_interface')
        self.assertEqual(oComponent.interfaces[0].name, 'source_interface')
        self.assertEqual(oComponent.interfaces[1].name, 'sink_interface')
        self.assertEqual(oIntSource.name, 'Interface1')
        self.assertEqual(oIntSink.name, 'Interface2')

    def test_component_get_interface_method(self):
        oIntSource = interface.create('Interface1')
        oIntSink = interface.create('Interface2')
        oComponent = component.create('component')
        oComponent.add_source_interface(oIntSource)
        oComponent.add_sink_interface(oIntSink)

        self.assertEqual(oComponent.get_interface('Interface1').name, 'Interface1')
        self.assertEqual(oComponent.get_interface('Interface2').name, 'Interface2')

if __name__ == '__main__':
    unittest.main()
