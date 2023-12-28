from solution_not import get_number_matches_from_line, get_symbol_locations_from_line, number_span_adjacent_to_symbol
import unittest

class TestSolution03(unittest.TestCase):
    def test_get_number_matches_from_line(self):
        line_no_symbols = '42...401.............425................963..420.....................697\n'
        expected_numbers_no_symbols = {'42': (0,2), '401': (5,8), '425': (21,24), '963': (40,43), '420': (45,48), '697': (69,72)}
        actual_iter = get_number_matches_from_line(line_no_symbols)
        self.assertEqual(True, self.actual_matches_match_expected(actual_iter, expected_numbers_no_symbols))

        line_symbols = '%21$..*.......\.290.=......%&$..../......492%...........#656@953........+7^\n'
        expected_numbers_line_symbols = {'21': (1,3), '290': (16,19), '492': (41,44), '656': (57,60), '953': (61,64), '7': (73, 74)}
        actual_iter = get_number_matches_from_line(line_symbols)
        self.assertEqual(True, self.actual_matches_match_expected(actual_iter, expected_numbers_line_symbols))


    """Verification helper method"""
    def actual_matches_match_expected(self, actual_iter, expected):
        for number_match in actual_iter:
            actual_number = number_match.group("number")
            if len(actual_number) > 0:
                number_span = number_match.span("number")
                if number_span != expected[actual_number]:
                    return False
        return True


    def test_get_symbol_locations_from_line(self):
        line_no_symbols = '42...401.............425................963..420.....................697\n'
        expected_no_symbols = []
        self.assertEqual(get_symbol_locations_from_line(line_no_symbols), expected_no_symbols)
        line_symbols = '%21$..*.......\.290.=......%&$..../......492%...........#656@953........+7^\n'
        expected_symbols = [0, 3, 6, 14, 20, 27, 28, 29, 34, 44, 56, 60, 72, 74]
        self.assertEqual(get_symbol_locations_from_line(line_symbols), expected_symbols)


    def test_number_span_adjacent_to_symbol(self):
        test_cases = {
            1: {"span": (1,1), "symbol_loc": 1, "expected": False},

            2: {"span": (0,3), "symbol_loc": 0, "expected": True},
            3: {"span": (1,3), "symbol_loc": 0, "expected": True},
            4: {"span": (2,3), "symbol_loc": 0, "expected": False},

            5: {"span": (1,2), "symbol_loc": 0, "expected": True},
            6: {"span": (1,2), "symbol_loc": 1, "expected": True},
            7: {"span": (1,2), "symbol_loc": 2, "expected": True},
            8: {"span": (1,2), "symbol_loc": 3, "expected": False},

            9: {"span": (2,5), "symbol_loc": 0, "expected": False},
            10: {"span": (2,5), "symbol_loc": 1, "expected": True},
            11: {"span": (2,5), "symbol_loc": 2, "expected": True},
            12: {"span": (2,5), "symbol_loc": 3, "expected": True},
            13: {"span": (2,5), "symbol_loc": 4, "expected": True},
            14: {"span": (2,5), "symbol_loc": 5, "expected": True},
            15: {"span": (2,5), "symbol_loc": 6, "expected": False},
            16: {"span": (2,5), "symbol_loc": 7, "expected": False},
        }
        for case_vals in test_cases.values():
            self.assertEqual(number_span_adjacent_to_symbol(case_vals["span"], case_vals["symbol_loc"]), case_vals["expected"])
        return

if __name__ == '__main__':
    unittest.main()