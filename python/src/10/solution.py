"""https://adventofcode.com/2023/day/10"""

import pathlib
from direction import Direction


def solve(file_name):
    s_node, sketch_lines = process_file(file_name)
    return get_farthest_steps_from_s(s_node, sketch_lines)


def get_farthest_steps_from_s(s_node, sketch_lines):
    next_nodes = get_next_nodes_from_node(s_node, sketch_lines)
    print(next_nodes)
    steps = 1

    while steps < 10:
        steps += 1
        print("Steps: " + str(steps))
        nodes_to_check = {}

        for direction, next_node in next_nodes.items():
            next_next_nodes = get_next_nodes_from_node(next_node, sketch_lines, direction)
            nodes_to_check = nodes_to_check | next_next_nodes

        print(nodes_to_check)
        if len(nodes_to_check) < 2:
            return steps

        next_nodes = nodes_to_check
    return False


def get_next_nodes_from_node(node, sketch_lines, direction = None):
    next_nodes = {}
    possible_directions = get_possible_directions_for_char(node)
    print(possible_directions)
    reverse_direction = get_reverse_direction(direction)
    if reverse_direction in possible_directions:
        print('in reverse direction removal')
        possible_directions.remove(reverse_direction)
    for direction in possible_directions:
        next_node = get_next_node_for_direction(node, direction, sketch_lines)
        if next_node != None:
            next_nodes[direction] = (next_node)
            print(next_nodes)
    return next_nodes


def get_reverse_direction(direction):
    if direction == Direction.NORTH:
        return Direction.SOUTH
    elif direction == Direction.SOUTH:
        return Direction.NORTH
    elif direction == Direction.EAST:
        return Direction.WEST
    elif direction == Direction.WEST:
        return Direction.EAST
    else:
        return False


def get_possible_directions_for_char(node):
    [x, y, char] = node
    if char == '|':
        return [Direction.NORTH, Direction.SOUTH]
    elif char == '-':
        return [Direction.EAST, Direction.WEST]
    elif char == 'L':
        return [Direction.NORTH, Direction.EAST]
    elif char == 'J':
        return [Direction.NORTH, Direction.WEST]
    elif char == '7':
        return [Direction.SOUTH, Direction.WEST]
    elif char == 'F':
        return [Direction.SOUTH, Direction.EAST]
    elif char == 'S':
        return [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
    else:
        return False


def get_next_node_for_direction(node, direction, sketch_lines):
    transformed_location, valid_chars_for_direction = get_directional_values(node, direction)
    if transformed_location != None:
        [x, y] = transformed_location
        char_at_location = sketch_lines[y][x]
        if char_at_location in valid_chars_for_direction:
            return (x, y, char_at_location)
    return None


def get_directional_values(node, direction):
    [x, y, char] = node
    transformed_location = None
    valid_chars_for_direction = None

    if direction == Direction.NORTH and y > 0:
        transformed_location = (x, y - 1)
        valid_chars_for_direction = '|F7'
    elif direction == Direction.EAST:
        transformed_location = (x + 1, y)
        valid_chars_for_direction = '-F7'
    elif direction == Direction.SOUTH:
        transformed_location = (x, y + 1)
        valid_chars_for_direction = '|LJ'
    elif direction == Direction.WEST and x > 0:
        transformed_location = (x - 1, y)
        valid_chars_for_direction = '-JE'
    
    return transformed_location, valid_chars_for_direction


def get_char_at_location(location, sketch_lines):
    [x, y, char] = location
    return sketch_lines[y][x]


def process_file(file_name):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        sketch_lines = []
        s_node = None
        line_index = 0

        while True:
            line = file.readline().replace('\n', '')
            if not line:
                break
        
            sketch_lines.append(line)

            if s_node == None:
                s_index = line.find('S')
                if s_index > -1:
                    s_node = (s_index, line_index, 'S')
                else:
                    line_index += 1

        return s_node, sketch_lines


print(solve('inputs/sample_02_simple.txt'))
