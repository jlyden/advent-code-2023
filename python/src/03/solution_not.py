"""https://adventofcode.com/2023/day/3
This never worked for full input, see solution.py
"""

import pathlib
import re


def solve(file_name):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        all_symbols_found = []
        found_part_numbers = []
        previous_line_candidates = {}
        previous_line_symbol_locations = []

        while True:
            line = file.readline()
            if not line:
                break

            number_matches = get_number_matches_from_line(line)
            this_line_symbol_locations = get_symbol_locations_from_line(line)

            part_numbers, this_line_candidates = check_current_line_for_part_numbers(number_matches, this_line_symbol_locations, previous_line_symbol_locations)
            found_part_numbers += part_numbers

            part_numbers = check_previous_line_for_part_numbers(previous_line_candidates, this_line_symbol_locations)
            found_part_numbers += part_numbers

            previous_line_candidates = this_line_candidates
            previous_line_symbol_locations = this_line_symbol_locations

    return sum(found_part_numbers)


def get_number_matches_from_line(line):
    return re.finditer(r'[^0-9]*(?P<number>[0-9]*)[^0-9]*', line)


def get_symbol_locations_from_line(line):
    symbol_matches = re.finditer(r'(?P<symbol>[^\.\d\n])', line)
    symbol_locations = list(map(lambda match: match.start(), symbol_matches))
    return symbol_locations


def check_current_line_for_part_numbers(number_matches, this_line_symbol_locations, previous_line_symbol_locations):
    part_numbers = []
    previous_line_candidates = {}

    for number_match in number_matches:
        possible_number = number_match.group('number')
        if len(possible_number) == 0:
            continue

        number_span = number_match.span('number')

        if number_span_adjacent_to_any_of_symbols(number_span, this_line_symbol_locations):
            part_numbers.append(int(possible_number))
        elif number_span_adjacent_to_any_of_symbols(number_span, previous_line_symbol_locations):
            part_numbers.append(int(possible_number))
        else:
            # Check with symbols from next line on next iteration
            previous_line_candidates[int(possible_number)] = number_span

    return part_numbers, previous_line_candidates


def check_previous_line_for_part_numbers(previous_line_candidates, symbol_locations):
    part_numbers = []

    if len(symbol_locations) == 0:
        return part_numbers

    for posible_number, number_span in previous_line_candidates.items():
        for symbol_location in symbol_locations:
            if number_span_adjacent_to_symbol(number_span, symbol_location):
                part_numbers.append(int(posible_number))
                break

    return part_numbers


def number_span_adjacent_to_any_of_symbols(number_span, symbol_locations):
    if len(symbol_locations) == 0:
        return False

    for symbol_location in symbol_locations:
        if number_span_adjacent_to_symbol(number_span, symbol_location):
            return True
    return False


"""unit tested"""
def number_span_adjacent_to_symbol(number_span, symbol_location):
    if number_span[0] == number_span[1]:
        # invalid span
        return False

    # handle diagonals
    start = number_span[0] - 1 if number_span[0] > 0 else number_span[0]
    end = number_span[1] + 1
    result = symbol_location in range(start, end)
    return result

solve('input.txt') # 4361 is correct sample result # wrong on input: 533728, 536236, 542484  