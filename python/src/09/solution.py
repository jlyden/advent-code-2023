"""https://adventofcode.com/2023/day/9"""

import pathlib


def solve(file_name, get_desired_element_of_history_func):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        history_sum = 0

        while True:
            line = file.readline().replace('\n', '')
            if not line:
                break

            history_sum += get_desired_element_of_history_func(line.split(' '))

    return history_sum


def get_previous_value_in_history(history):
    first_elements = [int(history[0])]
    level_diff = history

    while True:
        next_level_diff = get_diffs_for_list(level_diff)
        first_elements.append(next_level_diff[0])
        level_diff = next_level_diff

        diff_set = set(next_level_diff)
        if len(diff_set) == 1 and 0 in diff_set:
            break

    first_elements.reverse()
    to_subtract = first_elements.pop(0)
    for element in first_elements:
        next_element = element - to_subtract
        to_subtract = next_element
    
    return next_element


def get_next_value_in_history(history):
    last_elements = [int(history[-1])]
    level_diff = history

    while True:
        next_level_diff = get_diffs_for_list(level_diff)
        last_elements.append(next_level_diff[-1])
        level_diff = next_level_diff

        diff_set = set(next_level_diff)
        if len(diff_set) == 1 and 0 in diff_set:
            break

    return sum(last_elements)


def get_diffs_for_list(a_list):
    diffs = []
    previous_val = int(a_list.pop(0))
    for value in a_list:
        val = int(value)
        diffs.append(val - previous_val)
        previous_val = val
    return diffs

print(solve('input.txt', get_next_value_in_history))
print(solve('input.txt', get_previous_value_in_history))