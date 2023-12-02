"""https://adventofcode.com/2023/day/2"""

from functools import reduce
from operator import mul
import pathlib
import re

def get_sum(file_name, part):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        sum = 0

        while True:
            line = file.readline()
            if not line:
                break

            game_match = re.search(r"Game (?P<game_number>\d+): (?P<rounds>.+)", line)

            if part == 'part_one':
                if is_possible_game(game_match.group('rounds')):
                    sum += int(game_match.group('game_number'))
            else:
                minimum_cube_counts = get_minimum_required_cube_counts(game_match.group('rounds'))
                cube_power = reduce(mul, minimum_cube_counts, 1)
                sum += cube_power

    return sum

"""For Part One"""
def is_possible_game(game_rounds):
    cube_counts = {'red': 12, 'green': 13, 'blue': 14}

    rounds = game_rounds.split(';')
    for round in rounds:
        round_matches = re.finditer(r"(?P<count>\d+) (?P<color>\w*)", round)
        for match in round_matches:
            if cube_counts[match.group('color')] < int(match.group('count')):
                return False
    return True

"""For Part Two"""
def get_minimum_required_cube_counts(game_rounds):
    cube_counts = {'red': 0, 'green': 0, 'blue': 0}

    rounds = game_rounds.split(';')
    for round in rounds:
        round_matches = re.finditer(r"(?P<count>\d+) (?P<color>\w*)", round)
        for match in round_matches:
            round_count = int(match.group('count'))
            if round_count > cube_counts[match.group('color')]:
                cube_counts[match.group('color')] = round_count
    return cube_counts.values()

print(get_sum('input.txt', 'part_two'))