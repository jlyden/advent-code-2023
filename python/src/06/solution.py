"""https://adventofcode.com/2023/day/6"""

from functools import reduce
from operator import mul
import pathlib
import re

def solve_part_one(file_name):
    [times, records] = parse_input(file_name, 'part_one')
    wins_per_race = calculate_wins_per_race(times, records)
    return reduce(mul, wins_per_race, 1)

def solve_part_two(file_name):
    [times, records] = parse_input(file_name, 'part_two')
    wins_per_race = get_wins_for_race(times, records)
    return wins_per_race

def parse_input(input_file, part):
    [time_line, records_line] = get_contents_of_input_file(input_file)
    if part == 'part_one':
        times = re.findall(r"(?P<count>\d+)", time_line)
        records = re.findall(r"(?P<count>\d+)", records_line)
        return [times, records]
    else:
        time = int(time_line.split(':')[1].replace(' ', ''))
        record = int(records_line.split(':')[1].replace(' ', ''))
        return [time, record]

def get_wins_for_race(total_time, record):
    peak = total_time//2
    lowest_charge_to_win = find_lowest_charge_time_binary_search(1, peak, total_time, record)
    return calculate_wins(peak, lowest_charge_to_win, total_time)

def find_lowest_charge_time_binary_search(bottom, top, total_time, record):
    if (top - bottom) == 1:
        return top

    middle = bottom + ((top - bottom) // 2)
    charged_distance = get_charged_distance(total_time, middle)

    if charged_distance == record:
        return middle + 1
    elif charged_distance < record:
        bottom = middle
        return find_lowest_charge_time_binary_search(bottom, top, total_time, record)
    elif charged_distance > record:
        top = middle
        return find_lowest_charge_time_binary_search(bottom, top, total_time, record)

def calculate_wins_per_race(times, records):
    wins_per_race = []
    for index, time in enumerate(times):
        total_time = int(time)
        record = int(records[index])
        peak = total_time//2
        lowest_charge_to_win = find_lowest_charge_time_foreach(peak, total_time, record)
        wins = calculate_wins(peak, lowest_charge_to_win, total_time)
        wins_per_race.append(wins)
    return wins_per_race

def find_lowest_charge_time_foreach(peak, total_time, record):
    for charge_time in range(1, peak):
        charged_distance = get_charged_distance(total_time, charge_time)
        if record < charged_distance:
            return charge_time
    return False

def get_charged_distance(total_time, charging_time):
    return charging_time * (total_time - charging_time)

def calculate_wins(peak, first, total_time):
    wins = 0
    if is_even(total_time):
        wins = ((peak - first) * 2) + 1
    else:
        wins = (peak - first + 1) * 2
    return wins

def is_even(number):
    return number % 2 == 0

def get_contents_of_input_file(file_name):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        return file.readlines()

#print(solve_part_one('input.txt'))
print(solve_part_two('input.txt')) 