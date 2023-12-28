"""
https://adventofcode.com/2023/day/3
Second Attempt, different strategy - Part One complete
"""

import pathlib
import re

def solve_part_two(file_name):
    number_map, symbol_locations = process_file(file_name, part = 'part_two')
    gear_ratios = get_gear_ratios_for_asterisks(number_map, symbol_locations)
    return sum(gear_ratios)


def get_gear_ratios_for_asterisks(number_map, asterisk_locations):
    gear_ratios = []
    for asterisk_line, asterisks in asterisk_locations.items():
        # collect adjacent parts for each asterisk
        for asterisk in asterisks:
            part_numbers = []
            for number_line in [asterisk_line - 1, asterisk_line, asterisk_line + 1]:
                if number_line in number_map.keys():
                    for number_span, number in number_map[number_line].items():
                        if number_span_adjacent_to_symbol(number_span, asterisk):
                            part_numbers.append(int(number))
            if len(part_numbers) == 2:
                # this asterisk is a gear
                gear_ratios.append(part_numbers[0] * part_numbers[1])
    return gear_ratios


def solve_part_one(file_name):
    number_map, symbol_locations = process_file(file_name)
    part_numbers = find_part_numbers(number_map, symbol_locations)
    return sum(part_numbers)


def find_part_numbers(number_map, symbol_locations):
    part_numbers = []
    for line_index, line_number_map in number_map.items():
        if len(line_number_map) == 0:
            continue
        for number_span, number in line_number_map.items():
          symbol_locs_to_check = consolidate_symbol_locs_to_check_for_line(line_index, symbol_locations)
          for symbol_loc in symbol_locs_to_check:
              if number_span_adjacent_to_symbol(number_span, symbol_loc):
                  part_numbers.append(int(number))
    return part_numbers


def consolidate_symbol_locs_to_check_for_line(line_index, symbol_locations):
    symbol_locs = []
    # Need to check symbols on line_index +- 1
    for line in [line_index - 1, line_index, line_index + 1]:
        if line in symbol_locations.keys():
            symbol_locs = symbol_locs + symbol_locations[line]
    return symbol_locs


def number_span_adjacent_to_symbol(number_span, symbol_location):
    if number_span[0] == number_span[1]:
        # invalid span
        return False

    # handle diagonals
    start = number_span[0] - 1 if number_span[0] > 0 else number_span[0]
    end = number_span[1] + 1
    result = symbol_location in range(start, end)
    return result


def process_file(file_name, part = 'part_one'):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        number_map = {}
        symbol_locations = {}
        line_index = 0

        while True:
            line = file.readline()
            if not line:
                break
            
            number_matches = get_number_map_for_line(line)
            if len(number_matches) != 0:
                number_map[line_index] = number_matches
            symbol_locs = get_symbol_locations_for_line(line, part)
            if symbol_locs != None:
                symbol_locations[line_index] = symbol_locs
            line_index += 1

    return number_map, symbol_locations


def get_number_map_for_line(line):
    number_map_for_line = {}
    number_matches = re.finditer(r'[^0-9]*(?P<number>[0-9]*)[^0-9]*', line)
    for number_match in number_matches:
        number = number_match.group('number')
        if len(number) == 0:
            continue
        number_map_for_line[number_match.span('number')] = number
    return number_map_for_line


def get_symbol_locations_for_line(line, part = 'part_one'):
    if part == 'part_one':
        regex = '([^\.\d\n])'
    else:
        regex = '\*'
    symbol_matches = re.finditer(re.compile(regex), line)
    symbol_locations = list(map(lambda match: match.start(), symbol_matches))
    return symbol_locations if len(symbol_locations) > 0 else None


print(solve_part_one('input.txt')) # correct == 543867
print(solve_part_two('input.txt'))