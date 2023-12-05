"""https://adventofcode.com/2023/day/3"""

import pathlib
import re

"""Incomplete Part One. Working for sample input, but not full
Fixed one bug with symbol between two numbers
"""
def solve(file_name):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        found_part_numbers = []
        previous_line_candidates = {}
        previous_line_symbol_locations = []

        while True:
            line = file.readline().replace('\n', '')
            if not line:
                break

            number_matches = re.finditer(r"[^/.]\w*[^/.]", line)
            symbol_matches = re.finditer(r"(?P<symbol>[^\.\d\n])", line)
            this_line_symbol_locations = pull_symbol_locations_from_matches(symbol_matches)

            part_numbers, this_line_candidates = check_current_line_for_part_numbers(number_matches, this_line_symbol_locations, previous_line_symbol_locations)
            found_part_numbers += part_numbers

            part_numbers = check_previous_line_for_part_numbers(this_line_symbol_locations, previous_line_candidates)
            found_part_numbers += part_numbers

            previous_line_candidates = this_line_candidates
            previous_line_symbol_locations = this_line_symbol_locations

    print(found_part_numbers)
    return sum(found_part_numbers)


def pull_symbol_locations_from_matches(symbol_matches):
    symbol_locations = []
    for symbol_match in symbol_matches:
        symbol_locations.append(symbol_match.start())
    
    return symbol_locations


def check_current_line_for_part_numbers(number_matches, this_line_symbol_locations, previous_line_symbol_locations):
    part_numbers = []
    previous_line_candidates = {}

    for number_match in number_matches:
        possible_number = number_match.group(0)

        if match_has_adjacent_symbol(possible_number):
            only_number_match = re.search(r"\D*(?P<only_number>\d*)", possible_number)
            part_numbers.append(int(only_number_match.group('only_number')))
        else:
            number_span = number_match.span()

            if number_span_adjacent_to_any_of_symbols(number_span, this_line_symbol_locations):
                part_numbers.append(int(possible_number))
            elif number_span_adjacent_to_any_of_symbols(number_span, previous_line_symbol_locations):
                part_numbers.append(int(possible_number))
            else:
                # Check with symbols from next line on next iteration
                previous_line_candidates[int(possible_number)] = number_span

    return part_numbers, previous_line_candidates


def match_has_adjacent_symbol(possible_number):
    return not possible_number.isdigit()


def check_previous_line_for_part_numbers(symbol_locations, previous_line_candidates):
    part_numbers = []

    if len(symbol_locations) == 0:
        return part_numbers

    keys_to_remove_from_previous_line_candidates = []

    for symbol_location in symbol_locations:
        # remove keys surpassed after last iteration
        if len(keys_to_remove_from_previous_line_candidates) > 0:
            for key in keys_to_remove_from_previous_line_candidates:
                del previous_line_candidates[key]
        keys_to_remove_from_previous_line_candidates = []

        for posible_number, number_span in previous_line_candidates.items():
            if number_span_adjacent_to_symbol(number_span, symbol_location):
                part_numbers.append(int(posible_number))
                keys_to_remove_from_previous_line_candidates.append(posible_number)
                break

            # Plan to remove key if span is earlier than location now being checked
            if number_span[1] < symbol_location:
                keys_to_remove_from_previous_line_candidates.append(posible_number)
            continue

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
    return symbol_location in range(start, end)

print(solve('input_sample.txt')) # 533728 is too low, 536236 also wrong ): 