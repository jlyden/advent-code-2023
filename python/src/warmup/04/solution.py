"""https://adventofcode.com/2020/day/4"""

import pathlib
import validators

def get_count_of_valid_passports():
    lines = get_contents_of_input_file('input.txt')
    empty_line = ['\n']

    valid_passport_count = 0

    current_passport_dict = {}

    for line in lines:
        entries = line.split(' ')
        # if blank line, validate passport and reset current_passport_dict = {}
        if entries == empty_line:
            if is_valid_passport(current_passport_dict):
                valid_passport_count += 1
            # reset for next passport
            current_passport_dict = {}
            continue

        # collect keys from line
        for entry in entries:
            key, value = entry.split(':')
            current_passport_dict[key] = value.replace('\n', '')
    
    return valid_passport_count

def is_valid_passport(passport):
    required_passport_keys = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    for key in required_passport_keys:
        if key not in passport:
            return False
        isKeyValid = getattr(validators, f'evaluate_{key}')
        if isKeyValid(passport[key]) == False:
            return False
    return True

def get_count_of_valid_passports_key_check_only():
    lines = get_contents_of_input_file('input.txt')
    expected_passport_keys = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    expected_north_pole_creds_keys = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    empty_line = ['\n']

    valid_passport_count = 0

    current_passport_keys = []

    for line in lines:
        entries = line.split(' ')
        # if blank line, validate passport and reset current_passport_keys = []
        if entries == empty_line:
            current_passport_keys.sort()
            if (current_passport_keys == expected_passport_keys 
                or current_passport_keys == expected_north_pole_creds_keys):
                valid_passport_count += 1
            # reset for next passport
            current_passport_keys = []
            continue

        # collect keys from line
        for entry in entries:
            entry_parts = entry.split(':')
            current_passport_keys.append(entry_parts[0])
    
    return valid_passport_count

def get_contents_of_input_file(file_name):
    parent_dir = pathlib.Path(__file__).parent
    input_file = pathlib.PurePath(parent_dir, file_name)
    with open(input_file) as file:
        return file.readlines()

#print(get_count_of_valid_passports_key_check_only())

print(get_count_of_valid_passports())