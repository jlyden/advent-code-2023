"""https://adventofcode.com/2023/day/1"""

import pathlib

def get_sum_of_calibration_values(file_name, part):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        sum = 0

        while True:
            line = file.readline()
            if not line:
                break

            if part == 'part_two':
                digits = get_first_and_last_digits_with_word_numbers(line)
            else:
                digits = get_digits_from_string(line)
            print(digits)
            sum += get_number_from_digits(digits)
        
        return sum


"""For Part One"""
def get_digits_from_string(line):
    digits = ''
    for char in line:
        if char.isdigit():
            digits += char
    return digits


"""For Part Two"""
def get_first_and_last_digits_with_word_numbers(line):
    first_digit = get_first_digit(line)
    last_digit = get_last_digit(line)
    return first_digit + last_digit


def get_first_digit(line):
    word_numbers = {
        'o': [{'one': '1'}], 
        't': [{'two': '2'}, {'three': '3'}],
        'f': [{'four': '4'}, {'five': '5'}],
        's': [{'six': '6'}, {'seven': '7'}],
        'e': [{'eight': '8'}], 
        'n': [{'nine': '9'}],
    }
    return look_for_digits(line, word_numbers)


def get_last_digit(line):
    word_numbers_backwards = {
        'e': [{'eno': '1'}, {'eerht': '3'}, {'evif': '5'}, {'enin': '9'}],
        'o': [{'owt': '2'}],
        'r': [{'ruof': '4'}],
        'x': [{'xis': '6'}],
        'n': [{'neves': '7'}],
        't': [{'thgie': '8'}],
    }
    line_backwards = line[::-1]
    return look_for_digits(line_backwards, word_numbers_backwards)


def look_for_digits(line, word_numbers):
    for index, char in enumerate(line):
        # early exit for digit discovery
        if char.isdigit():
            return char

        if char in word_numbers.keys():
            possible_words = word_numbers[char]
            for option in possible_words:
                for key, value in option.items():
                    line_slice = line[index:index + len(key)]
                    if key == line_slice:
                        return value
    return 'oh $h1t'

"""For Both"""
def get_number_from_digits(digits):
    two_digit_string = ''
    if len(digits) == 1:
        two_digit_string = digits + digits
    elif len(digits) == 2:
        two_digit_string = digits
    else:
        two_digit_string = digits[0] + digits[-1]
    return int(two_digit_string)


print(get_sum_of_calibration_values('input.txt', 'part_one'))
print(get_sum_of_calibration_values('input.txt', 'part_two'))