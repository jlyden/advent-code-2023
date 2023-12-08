import unittest
from solution import process_line, get_type_of_hand_with_jokers

class TestSolution07(unittest.TestCase):
    joker_strengths = {
        'J': 'N', '2': 'M', '3': 'L', '4': 'K', '5': 'J', '6': 'I', '7': 'H', 
        '8': 'G', '9': 'F', 'T': 'E', 'Q': 'C', 'K': 'B', 'A': 'A'
    }

    def test_process_line_no_J(self):
        line_01 = '3Q373 470'
        expected_hand_type = 'three'
        expected_converted_hand = 'LCLHL'
        expected_bid = 470
        actual_hand_type, actual_converted_hand, actual_bid = process_line(line_01, get_type_of_hand_with_jokers, joker_strengths)
        self.assertEqual(actual_hand_type, expected_hand_type)
        self.assertEqual(actual_converted_hand, expected_converted_hand)
        self.assertEqual(actual_bid, expected_bid)

if __name__ == '__main__':
    unittest.main()