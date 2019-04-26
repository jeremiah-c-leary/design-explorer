
import unittest
import design_explorer as de


class test_connection(unittest.TestCase):

    def test_connection_class_attributes_exist(self):
        oComponent1 = de.component.create('Component1')
        oInterface1 = oComponent1.create_interface('Interface1')
        oInterface1.create_port('I1 P1', 1, 'out')
        oInterface1.create_port('I1 P2', 1, 'out')
        oInterface1.create_port('I1 P3', 1, 'out')
        oInterface1.create_port('I1 P4', 1, 'out')

        oComponent2 = de.component.create('Component2')
        oInterface2 = oComponent2.create_interface('Interface2')
        oInterface2.create_port('I2 P1', 1, 'out')
        oInterface2.create_port('I2 P2', 1, 'out')
        oInterface2.create_port('I2 P3', 1, 'out')
        oInterface2.create_port('I2 P4', 1, 'out')

        oConnection = de.connection.create('con1', oComponent1.get_interface_named('Interface1'), oComponent2.get_interface_named('Interface2'))

        self.assertEqual(oConnection.name, 'con1')
        self.assertEqual(oConnection.source.name, 'Interface1')
        self.assertEqual(oConnection.sink.name, 'Interface2')

        dMap = {}
        dMap['I1 P1'] = 'I2 P1'
        dMap['I1 P2'] = 'I2 P2'
        dMap['I1 P3'] = 'I2 P3'
        dMap['I1 P4'] = 'I2 P4'

        self.assertEqual(dMap, oConnection.map)

    def test_connection_map_port_method(self):
        oComponent1 = de.component.create('Component1')
        oInterface1 = oComponent1.create_interface('Interface1')
        oInterface1.create_port('I1 P1', 1, 'out')
        oInterface1.create_port('I1 P2', 1, 'out')
        oInterface1.create_port('I1 P3', 1, 'out')
        oInterface1.create_port('I1 P4', 1, 'out')

        oComponent2 = de.component.create('Component2')
        oInterface2 = oComponent2.create_interface('Interface2')
        oInterface2.create_port('I2 P1', 1, 'out')
        oInterface2.create_port('I2 P2', 1, 'out')
        oInterface2.create_port('I2 P3', 1, 'out')
        oInterface2.create_port('I2 P4', 1, 'out')

        oConnection = de.connection.create('con1', oComponent1.get_interface_named('Interface1'), oComponent2.get_interface_named('Interface2'), False)

        self.assertEqual(None, oConnection.map)

        oConnection.map_port('I1 P1', 'I2 P4')

        dMap = {}
        dMap['I1 P1'] = 'I2 P4'

        self.assertEqual(dMap, oConnection.map)


if __name__ == '__main__':
    unittest.main()
