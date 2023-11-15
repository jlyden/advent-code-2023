"""https://adventofcode.com/2020/day/1"""

import pathlib

def find_two_that_make_2020():
    lines = get_contents_of_input_file('input.txt')
    pairs = {}
    for line in lines:
        value = int(line.replace('\n',''))
        if value in pairs.keys():
            return value * pairs[value]
        pairs[2020-value] = value
    return False

def find_three_that_make_2020():
    lines = get_contents_of_input_file('input.txt')
    triples = {}
    candidates = []
    for line in lines:
        value = int(line.replace('\n',''))
        if value in triples.keys():
            return value * triples[value]
        for candidate in candidates:
            sum = value + candidate
            if sum < 2020:
                triples[2020-sum] = value * candidate
        candidates.append(value)
    return False

def get_contents_of_input_file(file_name):
    parent_dir = pathlib.Path(__file__).parents[0]
    input_file = pathlib.PurePath(parent_dir, file_name)
    with open(input_file) as file:
        return file.readlines()

print(find_three_that_make_2020())