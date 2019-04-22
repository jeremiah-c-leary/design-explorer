
import unittest
import design_explorer as de


class test_cca(unittest.TestCase):

    def test_cca_class_attributes_exist(self):
        oCca = de.hw.cca.create('cca1')
        self.assertEqual(oCca.name, 'cca1')
        self.assertEqual(oCca.components, None)
        self.assertEqual(oCca.connections, None)

    def test_cca_class_add_component_method(self):
        oCca = de.hw.cca.create('cca1')
        oCca.add_component('Component 1')
        oCca.add_component('Component 2')
        oCca.add_component('Component 3')
        self.assertEqual(len(oCca.components), 3)
        self.assertEqual(oCca.components[0], 'Component 1')
        self.assertEqual(oCca.components[1], 'Component 2')
        self.assertEqual(oCca.components[2], 'Component 3')

if __name__ == '__main__':
    unittest.main()
