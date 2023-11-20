"""https://adventofcode.com/2020/day/3"""

import pathlib
from functools import reduce

def calculate_tree_return_for_multiple_slopes(file_name):
    """We have to loop the slopes each time, but we only loop through input once"""
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        # Handle first line, setup vars
        first_line = file.readline()
        line_length = len(first_line)-1
        line_count = 0

        x_value_singles = [1, 3, 5, 7]
        x_value_double = 1

        x_positions_singles = [1, 3, 5, 7]
        tree_counts_singles = [0, 0, 0, 0]
        x_positions_double = 1
        tree_count_double = 0

        while True:
            line = file.readline()
            if not line:
                break

            line_count += 1

            for index, x_value in enumerate(x_value_singles):
                x_position = x_positions_singles[index]
                if line[x_position%line_length] == '#':
                    tree_counts_singles[index] += 1

                x_positions_singles[index] = x_position + x_value


            if line_count%2 == 0:
                if line[x_positions_double%line_length] == '#':
                    tree_count_double += 1
                x_positions_double += x_value_double

        tree_counts_singles.append(tree_count_double)

        return reduce(lambda x,y: x * y, tree_counts_singles)


def calculate_tree_return_for_all_passed_slopes(file_name):
    """Non-ideal solution ... involves looping file 5 times"""
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    slope_one_tree_count = get_count_of_trees_in_path(input_file, (1,1))
    slope_two_tree_count = get_count_of_trees_in_path(input_file, (3,1))
    slope_three_tree_count = get_count_of_trees_in_path(input_file, (5,1))
    slope_four_tree_count = get_count_of_trees_in_path(input_file, (7,1))
    slope_five_tree_count = get_count_of_trees_in_path(input_file, (1,2))
    return slope_one_tree_count * slope_two_tree_count * slope_three_tree_count * slope_four_tree_count * slope_five_tree_count

def get_count_of_trees_in_path(input_file, slope):
    """
    Args:
        input_file (file): file to read input from
        slope (tuple): right, down slope 

    Returns:
        tree_count (int): how many trees you hit when traversing input_file from 0,0 to final line
    """
    with open(input_file) as file:
        tree_count = 0
        x,y = slope

        # Handle first line
        first_line = file.readline()
        line_length = len(first_line)-1
        x_position = x

        line_count = None
        if y == 2:
            line_count = 0

        while True:
            line = file.readline()
            if not line:
                break

            if line_count != None:
                line_count += 1
                if line_count%2 == 1:
                    continue

            if line[x_position%line_length] == '#':
                tree_count += 1
            
            x_position += x

        return tree_count

def open_file_and_get_count_for_slope(file_name, slope):
    """
    Args:
        file_name (string): file to read input from
        slope (tuple): right, down slope 

    Returns:
        tree_count (int): how many trees you hit when traversing input_file from 0,0 to final line
    """
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    return get_count_of_trees_in_path(input_file, slope)

print(open_file_and_get_count_for_slope('input.txt', (3,1)))
print(calculate_tree_return_for_all_passed_slopes('input.txt'))
print(calculate_tree_return_for_multiple_slopes('input.txt'))