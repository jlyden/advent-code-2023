"""https://adventofcode.com/2020/day/6"""

import pathlib

def get_sum_of_questions_any_answered_yes():
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, 'input.txt')
    with open(input_file) as file:
        total_questions_groups_answered_yes = 0
        answers_from_group = ''

        while True:
            line = file.readline().replace('\n', '')
            if len(line) > 0:
                answers_from_group += line
            elif len(answers_from_group) == 0:
                break
            else:
                group_yes_count = len(set(answers_from_group))
                total_questions_groups_answered_yes += group_yes_count
                answers_from_group = ''

        return total_questions_groups_answered_yes

def get_sum_of_questions_all_answered_yes():
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, 'input.txt')
    with open(input_file) as file:
        total_questions_entire_groups_answered_yes = 0
        answers_from_group = ''
        size_of_group = 0

        while True:
            line = file.readline().replace('\n', '')
            if len(line) > 0:
                answers_from_group += line
                size_of_group += 1
            elif len(answers_from_group) == 0:
                break
            else:
                all_questions_answered = set(answers_from_group)
                group_yes_count = 0
                for question in all_questions_answered:
                    answer_count = answers_from_group.count(question)
                    if answer_count == size_of_group:
                        group_yes_count += 1
                total_questions_entire_groups_answered_yes += group_yes_count
                answers_from_group = ''
                size_of_group = 0

        return total_questions_entire_groups_answered_yes

#print(get_sum_of_questions_any_answered_yes())
print(get_sum_of_questions_all_answered_yes())