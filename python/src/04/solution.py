"""https://adventofcode.com/2023/day/4"""

import collections
import pathlib

def get_total(file_name, part):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        points_per_card = []

        while True:
            line = file.readline()
            if not line:
                break

            only_numbers = line.replace('\n', '').split(':')[1]
            winner_string, mine_string = only_numbers.split('|')

            winner_list = parse_numbers_in_string(winner_string)
            mine_list = parse_numbers_in_string(mine_string)

            result = collections.Counter(winner_list) & collections.Counter(mine_list)
            intersection = list(result.elements())
            points = 2**(len(intersection)-1) if len(intersection) > 0 else 0
            points_per_card.append(points)

        return sum(points_per_card)


def parse_numbers_in_string(number_string):
    list_with_empties = number_string.split(' ')
    return [x for x in list_with_empties if len(x) > 0]

print(get_total('input.txt', 'part_one'))