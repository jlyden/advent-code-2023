"""https://adventofcode.com/2020/day/8
Part One working below. Skipping pt 2 for now
"""

import pathlib
import re

def get_acc_value_before_loop():
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, 'input_sample.txt')
    instructions = parse_instructions(input_file)

    acc = 0
    index = 0
    while True:
        try:
            instruction = instructions[index]
        except KeyError:
            print('got to end')
            return acc

        if instruction['has_run'] == True:
            print('hit the loop')
            return acc

        if instruction['op'] == 'acc':
            acc = handle_math(acc, instruction['sign'], instruction['num'])
            instruction['has_run'] = True
            index += 1
            continue

        if instruction['op'] == 'jmp':
            index = handle_math(index, instruction['sign'], instruction['num'])
            instruction['has_run'] = True
            continue

        if instruction['op'] == 'nop':
            instruction['has_run'] = True
            index += 1
            continue

def handle_math(base, sign, num):
    if sign == '-':
        base -= num
    else:
        base += num
    return base

def parse_instructions(input_file):
    with open(input_file) as file:
        instructions = {}
        index = 0
        while True:
            line = file.readline()
            if not line:
                break

            match = re.search(r"(?P<op>\w+)\s(?P<sign>[+-])(?P<num>\d+)", line)
            instructions[index] = {
                'op': match.group('op'),
                'sign': match.group('sign'),
                'num': int(match.group('num')),
                'has_run': False,
            }
            index += 1

    return instructions

print(get_acc_value_before_loop())