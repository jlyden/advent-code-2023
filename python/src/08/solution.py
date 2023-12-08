"""https://adventofcode.com/2020/day/8"""

import pathlib
import re

def solve(file_name):
    left_right, nodes = process_input(file_name)
    return count_steps_to_travel_nodes(left_right, nodes)

def count_steps_to_travel_nodes(left_right, nodes):
    left_right_length = len(left_right)

    steps = 0
    left_right_index = 0
    current_node = 'AAA'

    while current_node != 'ZZZ':
        next_node = nodes[current_node][left_right[left_right_index]]

        current_node = next_node
        left_right_index += 1
        if left_right_index == left_right_length:
            left_right_index = 0
        steps += 1

    return steps

def process_input(file_name):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        nodes = {}
        first_line = list(file.readline().replace('\n', ''))
        left_right = [0 if char == 'L' else 1 for char in first_line]

        while True:
            line = file.readline()
            if not line:
                break

            match = re.search(r"(?P<name>\w*) = \((?P<left>\w*), (?P<right>\w*)", line)
            if match:
                nodes[match.group('name')] = (match.group('left'), match.group('right'))
    
    return left_right, nodes

print(solve('input.txt'))