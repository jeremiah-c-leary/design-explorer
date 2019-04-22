
import unittest
from design_explorer import component
from design_explorer import port
from design_explorer import interface


class test_hw_component(unittest.TestCase):

    def test_component_class_attributes_exist(self):
        oComponent = component.create('component1')
        self.assertEqual(oComponent.name, 'component1')
        self.assertEqual(oComponent.interfaces, None)
        self.assertEqual(oComponent.datasheet, None)

    def test_component_datasheet_attribute(self):
        oComponent = component.create('component1')
        oComponent.datasheet = 'datasheet url'
        self.assertEqual(oComponent.datasheet, 'datasheet url')

    def test_component_add_interface_method(self):
        oInterface1 = interface.create('Interface1')
        oInterface2 = interface.create('Interface2')
        oComponent = component.create('component')
        oComponent.add_interface(oInterface1)
        oComponent.add_interface(oInterface2)

        self.assertEqual(len(oComponent.interfaces), 2)
        self.assertEqual(oComponent.interfaces[0].name, 'Interface1')
        self.assertEqual(oComponent.interfaces[1].name, 'Interface2')

    def test_component_create_interface_method(self):
        oInterface1 = interface.create('Interface1')
        oInterface2 = interface.create('Interface2')
        oComponent = component.create('component')
        oInterface1 = oComponent.create_interface('Interface1')
        oInterface2 = oComponent.create_interface('Interface2')

        self.assertEqual(len(oComponent.interfaces), 2)
        self.assertEqual(oComponent.interfaces[0].name, 'Interface1')
        self.assertEqual(oComponent.interfaces[1].name, 'Interface2')
        self.assertEqual(oInterface1.name, 'Interface1')
        self.assertEqual(oInterface2.name, 'Interface2')

        oInterface1.name = 'New Interface1 Name'

        self.assertEqual(oComponent.interfaces[0].name, 'New Interface1 Name')
        self.assertEqual(oInterface1.name, 'New Interface1 Name')

    def test_component_get_interface_named_method(self):
        oIntSource = interface.create('Interface1')
        oIntSink = interface.create('Interface2')
        oComponent = component.create('component')
        oComponent.add_interface(oIntSource)
        oComponent.add_interface(oIntSink)

        self.assertEqual(oComponent.get_interface_named('Interface1').name, 'Interface1')
        self.assertEqual(oComponent.get_interface_named('Interface2').name, 'Interface2')
        self.assertEqual(oComponent.get_interface_named('Blah'), None)

if __name__ == '__main__':
    unittest.main()
