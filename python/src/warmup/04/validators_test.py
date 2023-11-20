import unittest
import validators

class TestValidators(unittest.TestCase):
    """evaluate_byr"""
    def test_evaluate_byr_valid(self):
        self.assertTrue(validators.evaluate_byr('1925'))

    def test_evaluate_byr_invalid_too_low(self):
        self.assertFalse(validators.evaluate_byr('1919'))

    def test_evaluate_byr_invalid_too_high(self):
        self.assertFalse(validators.evaluate_byr('2003'))

    """evaluate_ecl"""
    def test_evaluate_ecl_valid(self):
        for value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            self.assertTrue(validators.evaluate_ecl(value))

    def test_evaluate_ecl_invalid(self):
        self.assertFalse(validators.evaluate_ecl('abc'))

    """evaluate_eyr"""
    def test_evaluate_eyr_valid(self):
        self.assertTrue(validators.evaluate_eyr('2020'))

    def test_evaluate_eyr_invalid_too_low(self):
        self.assertFalse(validators.evaluate_eyr('2019'))

    def test_evaluate_eyr_invalid_too_high(self):
        self.assertFalse(validators.evaluate_eyr('2031'))

    """evaluate_hcl"""
    def test_evaluate_hcl_valid(self):
        self.assertTrue(validators.evaluate_hcl('#123abc'))

    def test_evaluate_hcl_invalid_no_hash(self):
        self.assertFalse(validators.evaluate_hcl('123abcd'))

    def test_evaluate_hcl_invalid_too_short(self):
        self.assertFalse(validators.evaluate_hcl('#123ab'))

    def test_evaluate_hcl_invalid_too_long(self):
        self.assertFalse(validators.evaluate_hcl('#123abcd'))

    def test_evaluate_hcl_invalid_wrong_char(self):
        self.assertFalse(validators.evaluate_hcl('#123abz'))

    """evaluate_hgt"""
    def test_evaluate_hgt_valid_cm(self):
        self.assertTrue(validators.evaluate_hgt('150cm'))

    def test_evaluate_hgt_valid_in(self):
        self.assertTrue(validators.evaluate_hgt('76in'))

    def test_evaluate_hgt_invalid_unit_unrecognized(self):
        self.assertFalse(validators.evaluate_hgt('76ab'))

    def test_evaluate_hgt_invalid_unit_missing(self):
        self.assertFalse(validators.evaluate_hgt('76'))

    def test_evaluate_hgt_invalid_measurement_not_number(self):
        self.assertFalse(validators.evaluate_hgt('7acm'))

    def test_evaluate_hgt_invalid_measurement_missing(self):
        self.assertFalse(validators.evaluate_hgt('cm'))

    def test_evaluate_hgt_invalid_cm_too_low(self):
        self.assertFalse(validators.evaluate_hgt('149cm'))

    def test_evaluate_hgt_invalid_cm_too_high(self):
        self.assertFalse(validators.evaluate_hgt('194cm'))

    def test_evaluate_hgt_invalid_in_too_low(self):
        self.assertFalse(validators.evaluate_hgt('58in'))

    def test_evaluate_hgt_invalid_in_too_high(self):
        self.assertFalse(validators.evaluate_hgt('77in'))

    """evaluate_iyr"""
    def test_evaluate_iyr_valid(self):
        self.assertTrue(validators.evaluate_iyr('2010'))

    def test_evaluate_iyr_invalid_too_low(self):
        self.assertFalse(validators.evaluate_iyr('2009'))

    def test_evaluate_iyr_invalid_too_high(self):
        self.assertFalse(validators.evaluate_iyr('2021'))

    """evaluate_pid"""
    def test_evaluate_pid_valid(self):
        self.assertTrue(validators.evaluate_pid('000000005'))

    def test_evaluate_iyr_invalid_too_short(self):
        self.assertFalse(validators.evaluate_iyr('12345678'))

    def test_evaluate_iyr_invalid_too_long(self):
        self.assertFalse(validators.evaluate_iyr('1234567899'))

    def test_evaluate_iyr_invalid_not_number(self):
        self.assertFalse(validators.evaluate_iyr('123456a89'))

    """evaluate_year_string"""
    def test_evaluate_year_string_valid(self):
        self.assertEqual(validators.evaluate_year_string('1905'), 1905)

    def test_evaluate_year_string_invalid_not_number(self):
        self.assertFalse(validators.evaluate_year_string('19a5'))

    def test_evaluate_year_string_invalid_too_long(self):
        self.assertFalse(validators.evaluate_year_string('192506'))
