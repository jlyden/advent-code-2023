"""https://adventofcode.com/2023/day/10"""

import pathlib
from direction import Direction


def solve(file_name):
    s_node, sketch_lines = process_file(file_name)
    return get_farthest_steps_from_s(s_node, sketch_lines)


def get_farthest_steps_from_s(s_node, sketch_lines):
    next_nodes = get_next_nodes_from_node(s_node, sketch_lines)
    steps = 1

    # ensure we don't end up in infinite loop
    while steps < 20000:
        steps += 1
        nodes_to_check = {}

        for direction, next_node in next_nodes.items():
            next_next_nodes = get_next_nodes_from_node(next_node, sketch_lines, direction)
            nodes_to_check = nodes_to_check | next_next_nodes

        if at_same_node(nodes_to_check):
            return steps

        # NOTE: this is a hack, but works
        # got back to start
        if len(nodes_to_check) == 0:
            return steps // 2

        next_nodes = nodes_to_check
    print(steps)
    return False


def at_same_node(nodes):
    if len(nodes) != 2:
        return False
    
    [node_one, node_two] = nodes.values()
    return node_one == node_two


def get_next_nodes_from_node(node, sketch_lines, direction = None):
    next_nodes = {}
    possible_directions = get_possible_directions_for_char(node)
    reverse_direction = get_reverse_direction(direction)
    if reverse_direction in possible_directions:
        possible_directions.remove(reverse_direction)
    for direction in possible_directions:
        next_node = get_next_node_for_direction(node, direction, sketch_lines)
        if next_node != None:
            next_nodes[direction] = (next_node)
    return next_nodes


def get_reverse_direction(direction):
    if direction == None:
        return None
    reverse_directions = {
        Direction.NORTH: Direction.SOUTH,
        Direction.SOUTH: Direction.NORTH,
        Direction.EAST: Direction.WEST,
        Direction.WEST: Direction.EAST,
    }
    return reverse_directions[direction]


def get_possible_directions_for_char(node):
    [x, y, char] = node
    char_to_dirs = {
        '|': [Direction.NORTH, Direction.SOUTH],
        '-': [Direction.EAST, Direction.WEST],
        'L': [Direction.NORTH, Direction.EAST],
        'J': [Direction.NORTH, Direction.WEST],
        '7': [Direction.SOUTH, Direction.WEST],
        'F': [Direction.SOUTH, Direction.EAST],
        'S': [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST],
    }
    return char_to_dirs[char]


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
        valid_chars_for_direction = '-J7'
    elif direction == Direction.SOUTH:
        transformed_location = (x, y + 1)
        valid_chars_for_direction = '|JL'
    elif direction == Direction.WEST and x > 0:
        transformed_location = (x - 1, y)
        valid_chars_for_direction = '-FL'
    
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


print(solve('inputs/input.txt'))
