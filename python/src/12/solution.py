"""https://adventofcode.com/2023/day/12"""

import pathlib
import re


def solve(file_name):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)

    with open(input_file) as file:
        arrangements = 0

        while True:
            line = file.readline()
            if not line:
                break

            spring_groups, counts = parse_line(line)
            arrangements += get_arrangements_for_line(spring_groups, counts)
        
        return arrangements


def get_arrangements_for_line(spring_groups, counts):
    if len(spring_groups) == len(counts):
        return get_arrangements_for_matched_lengths(spring_groups, counts)

    return get_arrangements_for_unmatched_lengths(spring_groups, counts)


# TODO: handle it
def get_arrangements_for_unmatched_lengths(spring_groups, counts):
    print('differing lengths of counts and matches')
    updated_spring_groups, updated_counts = remove_easy_matches(spring_groups, counts)
    print(updated_spring_groups)
    print(updated_counts)    

    return 0


def remove_easy_matches(spring_groups, counts):
    if len(spring_groups) == 1:
        # no easy matches
        return spring_groups, counts
    
    # taking an expensive shortcut here, will it bear out? I don't think so
    for count in counts:
        for index, count in enumerate(counts):
            for spring_group in spring_groups:
                if count == len(spring_group) and count == spring_group.count('#'):
                    counts.pop(index)
                    spring_groups.remove(spring_group)
    
    return spring_groups, counts



def get_arrangements_for_matched_lengths(spring_groups, counts):
    arrangements = 0
    for index, count in enumerate(counts):
        if count == len(spring_groups[index]):
            continue
        else:
            arrangements += calculate_simple_arrangements(count, spring_groups[index])
            continue
    return arrangements if arrangements > 0 else 1


def calculate_simple_arrangements(count, springs):
    return len(springs) // count


def parse_line(line):
    spring_portion, count_portion = line.split(' ')
    counts = [int(count) for count in count_portion.split(',') if True]
    springs = re.findall(r"\.?([#?]+)\.?", spring_portion)
    return springs, counts


print(solve('input_sample.txt'))