"""https://adventofcode.com/2020/day/5"""

import pathlib

def get_seat_id(which):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, 'input.txt')
    with open(input_file) as file:
        seat_ids = []

        row_bounds = 0, 127
        row_signals = 'F', 'B'
        seat_bounds = 0, 7
        seat_signals = 'L', 'R'

        while True:
            line = file.readline()
            if not line:
                break

            row_number = translate_string_to_number(line[0:7], row_bounds, row_signals)
            seat_number = translate_string_to_number(line[7:10], seat_bounds, seat_signals)

            seat_id = row_number * 8 + seat_number
            seat_ids.append(seat_id)
        
        seat_ids.sort()

        if which == 'highest':
            return seat_ids[-1]
        if which == 'mine':
            for index, seat_id in enumerate(seat_ids):
                if seat_ids[index+1] - seat_id == 2:
                    return seat_id + 1

def translate_string_to_number(value, bounds, signals):
    lower_bound, upper_bound = bounds
    lower_signal, upper_signal = signals

    middle = 0
    for char in value:
        middle = (upper_bound-lower_bound)//2 + lower_bound
        if char == lower_signal:
            upper_bound = middle
        if char == upper_signal:
            middle += 1
            lower_bound = middle
    return middle

print(get_seat_id('highest'))
print(get_seat_id('mine'))
