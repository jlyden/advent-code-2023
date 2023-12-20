"""https://adventofcode.com/2023/day/18
Incomplete
"""

import pathlib

def solve(file_name):
    instructions = process_file(file_name)
    return get_area_of_dig_plan(instructions)


def get_area_of_dig_plan(instructions):
    dimensions = build_dimensions_map(instructions)
    print(dimensions)
    return False
    #return calculate_area(dimensions)


def calculate_area(dimensions):
    area = 0
    current_y = 0
    previous_range = []
    for line, range in dimensions.items():
        while line > current_y:
            # repeat previous range for in between lines
            area += get_area_for_range(previous_range)
            current_y += 1

        # add range for this line
        area += get_area_for_range(range)
        previous_range = range
        current_y += 1
    return area


def get_area_for_range(range):
    [start, end] = range
    return end - start + 1


# TODO: this has problem
def build_dimensions_map(instructions):
    dimensions = {0: [0]}
    x = 0
    y = 0
    previous_y = 0
    for instruction in instructions:
        x, y = update_x_y_for_instruction(x, y, instruction)
        x_span = dimensions[y] if y in dimensions.keys() else None
        updated_x_span = get_new_x_span(x_span, x)
        dimensions[y] = updated_x_span

        if y != previous_y:
            if y > previous_y:
                start = previous_y
                end = y
            else:
                start = y
                end = previous_y
            for y_value in range(start, end):
                x_span = dimensions[y_value] if y_value in dimensions.keys() else None
                updated_x_span = get_new_x_span(x_span, x)
                dimensions[y_value] = updated_x_span
        print(dimensions)
    return dict(sorted(dimensions.items()))


def get_new_x_span(x_span, x):
    if x_span == None:
        return [x]
    
    x_span.append(x)
    x_span.sort()
    if len(x_span) > 2:
        del x_span[1]
    return x_span


def update_x_y_for_instruction(x, y, instruction):
    [direction, length] = instruction
    if direction == 'R':
        x += length
    elif direction == 'L':
        x -= length
    elif direction == 'D':
        y += length
    elif direction == 'U':
        y -= length
    return x, y


def process_file(file_name):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        instructions = []
        while True:
            line = file.readline()
            if not line:
                break

            parts = line.split(' ')
            instructions.append((parts[0], int(parts[1])))
        return instructions


print(solve('input_sample.txt'))