"""https://adventofcode.com/2023/day/15"""


import pathlib


def solve(file_name):
    input = get_contents_of_input_file(file_name)
    steps = input.split(',')
    current_values = [0]
    for step in steps:
        current_value = 0
        current_value = process_step(step, current_value)
        current_values.append(current_value)
    
    return sum(current_values)


def process_step(step, current_value):
    for char in step:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256

    return current_value


def get_contents_of_input_file(file_name):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        return file.readline().replace('\n', '')

print(solve('input.txt'))