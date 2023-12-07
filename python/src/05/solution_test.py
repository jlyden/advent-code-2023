import unittest
from solution import translate_map_line, process_value_with_map

class TestSolution05(unittest.TestCase):
    def test_translate_map_line_source_is_lower(self):
        test_line = "15 0 37\n"
        expected_range = (0, 37)
        expected_conversion = 15

        actual_range, actual_conversion = translate_map_line(test_line)
        self.assertEqual(actual_range, expected_range)
        self.assertEqual(actual_conversion, expected_conversion)

    def test_translate_map_line_destination_is_lower(self):
        test_line = "0 39 15\n"
        expected_range = (39, 54)
        expected_conversion = -39

        actual_range, actual_conversion = translate_map_line(test_line)
        self.assertEqual(actual_range, expected_range)
        self.assertEqual(actual_conversion, expected_conversion)

    def test_process_value_with_map(self):
        test_source = 79
        test_map = {(98, 100): -48, (50, 98): 2}
        expected = 81

        actual = process_value_with_map(test_source, test_map)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()