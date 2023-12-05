import unittest
from solution import number_span_adjacent_to_symbol, number_span_adjacent_to_any_of_symbols, check_previous_line_for_part_numbers

class TestSolution03(unittest.TestCase):
    def test_symbol_adjacent_to_number_span(self):
        self.assertEqual(number_span_adjacent_to_symbol((1,1), 1), False)

        self.assertEqual(number_span_adjacent_to_symbol((0,3), 0), True)
        self.assertEqual(number_span_adjacent_to_symbol((1,3), 0), True)
        self.assertEqual(number_span_adjacent_to_symbol((2,3), 0), False)

        self.assertEqual(number_span_adjacent_to_symbol((1,2), 0), True)
        self.assertEqual(number_span_adjacent_to_symbol((1,2), 1), True)
        self.assertEqual(number_span_adjacent_to_symbol((1,2), 2), True)
        self.assertEqual(number_span_adjacent_to_symbol((1,2), 3), False)

        self.assertEqual(number_span_adjacent_to_symbol((1,3), 1), True)
        self.assertEqual(number_span_adjacent_to_symbol((1,3), 2), True)
        self.assertEqual(number_span_adjacent_to_symbol((1,3), 3), True)
        self.assertEqual(number_span_adjacent_to_symbol((1,3), 4), False)

        self.assertEqual(number_span_adjacent_to_symbol((1,4), 1), True)
        self.assertEqual(number_span_adjacent_to_symbol((1,4), 2), True)
        self.assertEqual(number_span_adjacent_to_symbol((1,4), 3), True)
        self.assertEqual(number_span_adjacent_to_symbol((1,4), 4), True)
        self.assertEqual(number_span_adjacent_to_symbol((1,4), 5), False)

if __name__ == '__main__':
    unittest.main()