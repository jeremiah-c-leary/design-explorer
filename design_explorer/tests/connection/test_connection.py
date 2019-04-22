
import unittest
import design_explorer as de


class test_connection(unittest.TestCase):

    def test_connection_class_attributes_exist(self):
        oComponent1 = de.component.create('Component1')
        oComponent1.create_interface('Interface1')

        oComponent2 = de.component.create('Component2')
        oComponent2.create_interface('Interface2')

        oConnection = de.connection.create(oComponent1.get_interface_named('Interface1'), oComponent2.get_interface_named('Interface2'))

        self.assertEqual(oConnection.name, None)
        self.assertEqual(oConnection.source.name, 'Interface1')
        self.assertEqual(oConnection.sink.name, 'Interface2')

        oConnection.name = 'Named connection'

        self.assertEqual(oConnection.name, 'Named connection')

if __name__ == '__main__':
    unittest.main()
