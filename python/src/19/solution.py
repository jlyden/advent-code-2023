"""https://adventofcode.com/2023/day/19"""

import pathlib
import re


def solve(file_name):
    workflows, parts = process_file(file_name)
    accepted_parts = get_accepted_parts(workflows, parts)
    return sum_parts_attributes(accepted_parts)


def sum_parts_attributes(parts):
    total = 0
    for part in parts:
        total += sum(part.values())
    return total


def get_accepted_parts(workflows, parts):
    accepted_parts = []
    for part in parts:
        next = 'in'
        while next not in ['A', 'R']:
            next = run_workflow(workflows[next], part)
            if next == 'A':
                accepted_parts.append(part)
    return accepted_parts


def run_workflow(flow, part):
    for step in flow:
        keys = step.keys()
        if 'att' in keys:
            att = step['att']
            if step['comp'] == 'lt':
                if part[att] < step['val']:
                    return step['next']
            else:
                if part[att] > step['val']:
                    return step['next']
        elif len(keys) == 1 and 'next' in keys:
            return step['next']
    return None


def process_file(file_name):
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        workflows = {}
        parts = []

        while True:
            line = file.readline()
            if not line:
                break

            if line[0] == '{':
                parts.append(process_part(line))
            elif len(line) > 1:
                workflows.update(process_workflow(line))
        return workflows, parts


def process_workflow(line):
    steps = []
    [name, flow] = line.replace('}\n', '').split('{')
    for flow_step in flow.split(','):
        if '<' in flow_step:
            matches = re.search(r"(?P<att>\w)<(?P<val>\d*):(?P<next>\w*)", flow_step)
            comp = 'lt'
        elif '>' in flow_step:
            matches = re.search(r"(?P<att>\w)>(?P<val>\d*):(?P<next>\w*)", flow_step)
            comp = 'gt'
        else:
            matches = None
            steps.append({'next': flow_step})
        
        if matches != None:
            att = matches.group('att')
            val = int(matches.group('val'))
            next = matches.group('next')
            steps.append({'att': att, 'comp': comp, 'val': val, 'next': next})
    return {name: steps}


def process_part(line):
    attributes = {}
    matches = re.search(r"{x=(?P<x>\d*),m=(?P<m>\d*),a=(?P<a>\d*),s=(?P<s>\d*)}", line)
    for att in ['x', 'm', 'a', 's']:
        attributes[att] = int(matches.group(att))
    return attributes


print(solve('input.txt'))