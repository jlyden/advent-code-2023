"""https://adventofcode.com/2023/day/4"""

import collections
import pathlib

def get_total(file_name, part):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)

    with open(input_file) as file:
        points_per_card = []
        winners_per_card = []

        while True:
            line = file.readline()
            if not line:
                break

            only_numbers = line.replace('\n', '').split(':')[1]
            winner_string, mine_string = only_numbers.split('|')

            winner_list = parse_numbers_in_string(winner_string)
            mine_list = parse_numbers_in_string(mine_string)

            result = collections.Counter(winner_list) & collections.Counter(mine_list)
            count_winners = len(list(result.elements()))

            if part == 'part_one':
                points = 2**(count_winners-1) if count_winners > 0 else 0
                points_per_card.append(points)
            else:
                winners_per_card.append(count_winners)

        if part == 'part_one':
            return sum(points_per_card)
        else:
            return find_total_cards(winners_per_card)


def parse_numbers_in_string(number_string):
    list_with_empties = number_string.split(' ')
    return [x for x in list_with_empties if len(x) > 0]

"""Part Two Only"""
def find_total_cards(winners_per_card):
    total_cards = 0
    future_cards = {}

    for index, future_dups in enumerate(winners_per_card):
        if index not in future_cards.keys():
            future_cards[index] = 0

        total_copies_of_this_card = 1 + future_cards[index]
        total_cards += total_copies_of_this_card

        # add later bonus cards based on these wins
        if future_dups > 0:
            for i in range(1, future_dups+1):
                future_card_key = index + i
                if future_card_key in future_cards:
                    future_cards[future_card_key] += total_copies_of_this_card
                else:
                    future_cards[future_card_key] = total_copies_of_this_card

    return total_cards

print(get_total('input.txt', 'part_two'))