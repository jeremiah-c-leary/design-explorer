
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

    def test_trim_path_to_level(self):
        sInput = 'top.cca1.cca2.cca3.comp2.i1'
        self.assertEqual('top.cca1.cca2', de.utils.trim_path_to_level(sInput, 2))

    def test_remove_first_element_from_path(self):
        sInput = 'top.cca1.cca2.cca3.comp2.i1'
        self.assertEqual('cca1.cca2.cca3.comp2.i1', de.utils.remove_first_element_from_path(sInput))

    def test_remove_last_element_from_path(self):
        sInput = 'top.cca1.cca2.cca3.comp2'
        self.assertEqual('top.cca1.cca2.cca3', de.utils.remove_last_element_from_path(sInput))

if __name__ == '__main__':
    unittest.main()
