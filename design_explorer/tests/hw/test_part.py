
import unittest
from design_explorer.hw import part


class test_hw_part(unittest.TestCase):

    def test_part_class_attributes_exist(self):
        oPart = part.create('part1')
        self.assertEqual(oPart.name, 'part1')
        self.assertEqual(oPart.manufacturer, None)
        self.assertEqual(oPart.partNumber, None)


if __name__ == '__main__':
    unittest.main()
