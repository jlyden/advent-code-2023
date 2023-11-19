"""https://adventofcode.com/2020/day/2"""

import pathlib

def get_count_of_valid_passwords(file_name, is_password_valid_callback):
    """Validates passwords in input based on callback
    Args:
        file_name (string): file to read input from
        is_password_valid_callback (function): function to use for password validation

    Returns:
        valid_password_count (int)
    """
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        valid_password_count = 0

        while True:
            line = file.readline()
            if not line:
                break
            
            line_parts = line.split(' ')
            first, second = line_parts[0].split('-')
            first, second = int(first), int(second)
            target_char = line_parts[1][0]
            password = line_parts[2]

            if is_password_valid_callback(first, second, target_char, password):
                valid_password_count += 1

    return valid_password_count

def is_valid_password_char_position(first, second, target_char, password):
    """Returns True if target_char is at password[first] XOR password[second]
    NOTE: first and second are one-indexed, not zero-indexed, so require normalization
    
    Args:
    first (int): first index to check
    second (int): second index to check
    target_char (string): char to check for
    first (string): password to apply indexes to
    """
    password_char_first = password[first - 1]
    password_char_second = password[second - 1]
    if password_char_first != password_char_second and target_char in [password_char_first, password_char_second]:
        return True
    return False

def is_valid_password_char_count(first, second, target_char, password):
    """Returns True if count(target_char) >= first and <= second in password

    Args:
    first (int): lower bound (inclusive)
    second (int): upper bound inclusive
    target_char (string): char to check for
    first (string): password to apply indexes to
    """
    target_char_count = 0
    valid = True
    for char in password:
        if char == target_char:
            target_char_count += 1
            if target_char_count > second:
                valid = False
                break

    if valid and target_char_count >= first:
        return True
    
    return False

print(get_count_of_valid_passwords('input.txt', is_valid_password_char_count))

print(get_count_of_valid_passwords('input.txt', is_valid_password_char_position))