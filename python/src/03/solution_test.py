import unittest
from solution import number_span_adjacent_to_symbol, get_symbol_locations_from_line, get_number_matches_from_line

class TestSolution03(unittest.TestCase):
    def test_get_number_matches_from_line_only_numbers(self):
        line_no_symbols = '....401.............425........697...............963...................................420.....................\n'
        expected = {'401': (4,7), '425': (20,23), '697': (31,34), '963': (49,52), '420': (87,90)}
        actual_iter = get_number_matches_from_line(line_no_symbols)
        for number_match in actual_iter:
            actual_number = number_match.group(0)
            number_span = number_match.span()
            self.assertEqual(expected[actual_number], number_span)

    def test_get_number_matches_from_line_numbers_and_symbols(self):
        line_symbols = '...*....*....290..................%......#.........492%.............#656@953........................+830.........\n'
        #expected = {401: (4,7), 425: (20,23), 697: (31,34), 963: (49,52), 420: (87,90)}
        actual_iter = get_number_matches_from_line(line_symbols)
        for number_match in actual_iter:
            actual_number = number_match.group(0)
            number_span = number_match.span()
            print(actual_number, number_span)
            #self.assertEqual(expected[actual_number], number_span)

    def test_get_symbol_locations_from_line(self):
        line_no_symbols = '....401.............425........697...............963...................................420.....................\n'
        expected_no_symbols = []
        self.assertEqual(get_symbol_locations_from_line(line_no_symbols), expected_no_symbols)

        line_symbols = '...*....*....290..................%......#.........492%.............#656@953........................+830.........\n'
        expected_symbols = [3, 8, 34, 41, 54, 68, 72, 100]
        self.assertEqual(get_symbol_locations_from_line(line_symbols), expected_symbols)

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