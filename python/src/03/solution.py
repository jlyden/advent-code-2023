"""https://adventofcode.com/2023/day/3"""

import pathlib
import re

"""Incomplete Part One. Working for sample input,
returning 533728 for full input which is too low
"""
def solve(file_name):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        found_part_numbers = []
        previous_line_candidates = {}
        previous_line_symbol_locations = []

        while True:
            line = file.readline()
            if not line:
                break

            number_matches = re.finditer(r"[^/.]\w*[^/.]", line)
            symbol_matches = re.finditer(r"(?P<symbol>[^\.\d\n])", line)

            part_numbers, this_line_candidates = check_current_line_for_part_numbers(number_matches, previous_line_symbol_locations)
            found_part_numbers += part_numbers

            part_numbers, this_line_symbol_locations = check_previous_line_for_part_numbers(symbol_matches, previous_line_candidates)
            found_part_numbers += part_numbers

            previous_line_candidates = this_line_candidates
            previous_line_symbol_locations = this_line_symbol_locations

    return sum(found_part_numbers)


def check_current_line_for_part_numbers(number_matches, previous_line_symbol_locations):
    part_numbers = []
    previous_line_candidates = {}

    # for each number match in line
    for number_match in number_matches:
        possible_part = number_match.group(0)

        # this is a hit with current-line symbols
        if match_has_adjacent_symbol(possible_part):
            only_number_match = re.search(r"\D*(?P<only_number>\d*)", possible_part)
            part_numbers.append(int(only_number_match.group('only_number')))
        else:
            number_span = number_match.span()
            # look for hit with previous line symbols
            if number_span_adjacent_to_previous_line_symbols(previous_line_symbol_locations, number_span):
                part_numbers.append(int(possible_part))
            else:
                # check this number in the next iteration
                previous_line_candidates[int(possible_part)] = number_span

    return part_numbers, previous_line_candidates


def match_has_adjacent_symbol(possible_part):
    return not possible_part.isdigit()


def check_previous_line_for_part_numbers(symbol_matches, previous_line_candidates):
    part_numbers = []
    this_line_symbol_locations = []

    if symbol_matches == None:
        return part_numbers, this_line_symbol_locations

    keys_to_remove_from_dict = []

    # for each symbol match in line
    for match in symbol_matches:
        symbol_location = match.start()

        # remove keys surpassed after last iteration
        if len(keys_to_remove_from_dict) > 0:
            for key in keys_to_remove_from_dict:
                del previous_line_candidates[key]
        keys_to_remove_from_dict = []

        # for each possible part number on previous line
        for number, number_span in previous_line_candidates.items():
            if symbol_adjacent_to_number_span(number_span, symbol_location):
                part_numbers.append(int(number))
                keys_to_remove_from_dict.append(number)
                break

            # Stop checking this number
            if number_span[1] < symbol_location:
                keys_to_remove_from_dict.append(number)
            continue

        this_line_symbol_locations.append(symbol_location)

    return part_numbers, this_line_symbol_locations


def number_span_adjacent_to_previous_line_symbols(previous_line_symbol_locations, number_span):
    # for each symbol path in previous line
    for symbol_location in previous_line_symbol_locations:
        if symbol_adjacent_to_number_span(number_span, symbol_location):
            return True
    return False


def symbol_adjacent_to_number_span(number_span, symbol_location):
    # handle diagonals
    start = number_span[0] - 1 if number_span[0] > 0 else number_span[0]
    end = number_span[1] + 1
    return symbol_location in range(start, end)

print(solve('input_sample.txt')) # 533728 is too low