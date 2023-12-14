"""https://adventofcode.com/2023/day/11"""

import pathlib
import re


def solve(file_name):
    expanded_galaxy_coords = process_file(file_name)
    print(expanded_galaxy_coords)
    distances = calculate_distances_between_all_galaxies(expanded_galaxy_coords)
    return sum(distances)


def calculate_distances_between_all_galaxies(galaxy_coords):
    distances = []
    for row, cols in galaxy_coords.items():
        row_distances = calculate_galaxy_distances_for_row_galaxies(row, cols, galaxy_coords)
        distances = distances + row_distances
    return distances


def calculate_galaxy_distances_for_row_galaxies(row, cols, galaxy_coords):

    return False


def calculate_distances_between_two_galaxies(galaxy_one, galaxy_two):

    return False


def process_file(file_name):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        galaxy_coords = {}
        cols_with_galaxies = []
        row_index = 0

        first_line = file.readline().replace('\n', '')
        col_count = len(first_line)

        col_indices = get_galaxy_indices_on_line(first_line)
        cols_with_galaxies = cols_with_galaxies + col_indices
        galaxy_coords[row_index] = col_indices

        while True:
            line = file.readline().replace('\n', '')
            if not line:
                break
        
            row_index += 1
            col_indices = get_galaxy_indices_on_line(line)
            cols_with_galaxies += col_indices
            galaxy_coords[row_index] = col_indices

        col_range = range(col_count)
        all_cols = [*col_range]
        cols_no_galaxies = sorted(list(set(all_cols) - set(cols_with_galaxies)))
        return expand_the_universe(galaxy_coords, cols_no_galaxies)


def expand_the_universe(galaxy_coords, cols_no_galaxies):
    expanded_galaxy_coords = {}
    row_expansion = 0
    for row, galaxy_cols in galaxy_coords.items():
        expanded_galaxy_cols = []
        if len(galaxy_cols) == 0:
            row_expansion += 1
        # nested loops == bad bad bad
        for galaxy in galaxy_cols:
            updated_galaxy = galaxy
            for col in cols_no_galaxies:
                if galaxy > col:
                    updated_galaxy += 1
            expanded_galaxy_cols.append(updated_galaxy)
        expanded_galaxy_coords[row + row_expansion] = expanded_galaxy_cols
    return expanded_galaxy_coords


def get_galaxy_indices_on_line(line):
    col_indices = []
    galaxy_matches = re.finditer(r"\#", line)
    for galaxy_match in galaxy_matches:
        col_indices.append(galaxy_match.start())
    return col_indices

print(solve('input_sample.txt'))
