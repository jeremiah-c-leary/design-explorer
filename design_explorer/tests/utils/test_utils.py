
import unittest
import design_explorer as de


class test_functions(unittest.TestCase):


    def test_extract_interface_from_path(self):
        sInput = 'cca1.cca2.cca3.comp1.I1'
        sExpected = 'I1'
        self.assertEqual(sExpected, de.utils.extract_interface_from_path(sInput))


    def test_extract_component_from_path(self):
        sInput = 'cca1.cca2.cca3.comp1.I1'
        sExpected = 'comp1'
        self.assertEqual(sExpected, de.utils.extract_component_from_path(sInput))


    def test_remove_interface_from_path(self):
        sInput = 'cca1.cca2.cca3.comp1.I1'
        sExpected = 'cca1.cca2.cca3.comp1'
        self.assertEqual(sExpected, de.utils.remove_interface_from_path(sInput))
        

if __name__ == '__main__':
    unittest.main()
