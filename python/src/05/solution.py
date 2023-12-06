"""https://adventofcode.com/2023/day/5

Part One is done. 
Part Two brute force won't work (too many seeds) ...
need completely different approach
"""

import pathlib

def solve(file_name):
    seeds, almanac = parse_almanac(file_name)
    seed_locations = get_corresponding_seed_locations(seeds, almanac)
    return min(seed_locations)


def get_corresponding_seed_locations(seeds, almanac):
    seed_locations = []

    for seed in seeds:
        destination = seed
        # Since Python 3.7, dicts are ordered
        # https://docs.python.org/3.12/library/stdtypes.html#dict
        for map in almanac.values():
            destination = process_value_with_map(destination, map)
        seed_locations.append(destination)
    return seed_locations


def process_value_with_map(source, map):
    """Returns destination associated with source based on map
    If source not in map range, return source

    Args:
        map: {range_tuple: integer_offset, ...}
        seed: number that may appear in one of range_tuple(s)

    Returns:
        number
    """
    for range_tuple, offset in map.items():
        [start, end] = range_tuple
        if source in range(start, end):
            return source + offset

    return source


def parse_almanac(file_name):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        seeds = []
        almanac = {}
        map_in_progress = ''

        while True:
            line = file.readline()
            if not line:
                break

            if 'seeds:' in line:
                seeds = parse_seeds(line)
            elif 'map:' in line:
                map_title = line.split(' ')[0]
                map_in_progress = map_title
                almanac[map_in_progress] = {}
            elif line == '\n':
                map_in_progress = ''
            else:
                range_tuple, conversion = translate_map_line(line)
                almanac[map_in_progress][range_tuple] = conversion

        return seeds, almanac


def parse_seeds(seeds_line):
    numerics = seeds_line.replace('\n', '').split(':')[1].strip().split(' ')
    return [int(numeric.strip()) for numeric in numerics if True]


def translate_map_line(line):
    """Translates string line into usable map
    unittested

    Args:
        line: string sequence of three numbers

    Returns:
        tuple, number
    """
    raw_numbers = line.replace('\n', '').split(' ')
    [destination_start, source_start, range] = [int(raw.strip()) for raw in raw_numbers if True]
    range_tuple = source_start, source_start + range
    destination_source_diff = destination_start - source_start
    conversion = destination_source_diff if destination_start > source_start else -abs(destination_source_diff)
    return range_tuple, conversion


def get_contents_of_input_file(file_name):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        return file.readlines()

print(solve('input.txt'))