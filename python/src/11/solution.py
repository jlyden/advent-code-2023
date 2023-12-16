"""https://adventofcode.com/2023/day/11"""

import pathlib
import re


def solve(file_name):
    expanded_galaxy_coords = process_file(file_name)
    distances = calculate_distances_between_all_galaxies(expanded_galaxy_coords)
    return sum(distances)


def calculate_distances_between_all_galaxies(galaxy_coords):
    distances = []
    for row in galaxy_coords.keys():
        row_distances = calculate_galaxy_distances_for_row(row, galaxy_coords)
        distances = distances + row_distances
        # we've processed this row's galaxies ... don't come back to them 
        galaxy_coords[row] = []
    return distances


def calculate_galaxy_distances_for_row(row, galaxy_coords):
    distances = []
    cols = galaxy_coords[row]
    is_multi_galaxy_row = False
    if len(cols) > 1:
        is_multi_galaxy_row = True
        same_row_distances = calculate_galaxy_distances_for_cols_in_same_row(cols)
        distances = distances + same_row_distances
    for col in cols:
        col_distances = calculate_galaxy_distances_for_col(row, col, galaxy_coords, is_multi_galaxy_row)
        distances = distances + col_distances
    return distances


def calculate_galaxy_distances_for_col(low_row, low_col, galaxy_coords, is_multi_galaxy_row):
    distances = []
    # holy crap more nested loops
    for row, cols in galaxy_coords.items():
        if is_multi_galaxy_row and row == low_row:
            # Will calculate separately for same-row galaxies
            continue
        elif len(cols) > 0:
            for col in cols:
                distance = abs(row - low_row) + abs(col - low_col)
                distances.append(distance)
    return distances


def calculate_galaxy_distances_for_cols_in_same_row(cols):
    distances = []
    for index, col in enumerate(cols):
        rest_of_col = cols[index:]
        index_distances = list(map(lambda x: (x - col), rest_of_col))
        distances = distances + index_distances
    return distances


def process_file(file_name):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        galaxy_coords = {}
        cols_with_galaxies = []
        row_index = 0

        while True:
            line = file.readline().replace('\n', '')
            if not line:
                break
        
            col_indices = get_galaxy_indices_on_line(line)
            if len(col_indices) == 0:
                # handle vertical expansion (of rows) with bonus bump
                row_index += 1
            else:
                galaxy_coords[row_index] = col_indices
                cols_with_galaxies += col_indices
            row_index += 1

        return expand_the_universe_horizontally(galaxy_coords, cols_with_galaxies)


def expand_the_universe_horizontally(galaxy_coords, cols_with_galaxies):
    expanded_galaxy_coords = {}
    row_expansion = 0
    cols_no_galaxies = get_cols_without_galaxies(cols_with_galaxies)

    for row, galaxy_cols in galaxy_coords.items():
        expanded_galaxy_cols = []
        # nested loops == bad bad bad
        for galaxy in galaxy_cols:
            updated_galaxy = galaxy
            for col in cols_no_galaxies:
                if galaxy > col:
                    updated_galaxy += 1
            expanded_galaxy_cols.append(updated_galaxy)
        expanded_galaxy_coords[row + row_expansion] = expanded_galaxy_cols
    return expanded_galaxy_coords


def get_cols_without_galaxies(cols_with_galaxies):
    cols_with_galaxies.sort()
    last_col = cols_with_galaxies[-1]
    col_range = range(last_col)
    all_cols = [*col_range]
    return sorted(list(set(all_cols) - set(cols_with_galaxies)))


def get_galaxy_indices_on_line(line):
    col_indices = []
    galaxy_matches = re.finditer(r"\#", line)
    for galaxy_match in galaxy_matches:
        col_indices.append(galaxy_match.start())
    return col_indices


print(solve('input_sample.txt'))
