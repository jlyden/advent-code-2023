"""https://adventofcode.com/2020/day/7"""

import pathlib

def get_count_of_bag_colors_holding_shiny_gold_bags():
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, 'input.txt')
    rules_dict = build_rules_dict_from_input_file(input_file)
    return get_gold_bag_holders_count(rules_dict)

def get_gold_bag_holders_count(rules_dict):
    bag_holders = find_bag_holders(rules_dict, 'shiny gold')
    holder_len_before = len(bag_holders)
    while True:
        more_holders = []
        for bag in bag_holders:
            more_holders += find_bag_holders(rules_dict, bag)
        bag_holders = list(set(bag_holders + more_holders))
        holder_len_now = len(bag_holders)
        if holder_len_now == holder_len_before:
            break
        else:
            holder_len_before = holder_len_now
    return holder_len_now

def find_bag_holders(rules_dict, bag_to_hold):
    more_holders = []
    rules_keys = rules_dict.keys()
    for key in rules_keys:
        if bag_to_hold in rules_dict[key].keys():
            more_holders.append(key)
    return list(set(more_holders))

def build_rules_dict_from_input_file(input_file):
    with open(input_file) as file:
        rules_dict = {}
        while True:
            line = file.readline()
            if not line:
                break

            key, values = parse_rule(line)
            if len(values) > 0:
                rules_dict[key] = values
    return rules_dict

# This works, but regex would be nice
"""
This matches bags with multiple interior bags, but not empty bags or bags with one interior bag
"(?P<bag_holder>\w*\s\w*)\sbags contain\s(?P<one_count>\d)\s(?P<one_color>\w*\s\w*)\sbags?[,.]\s(?P<two_count>\d)\s(?P<two_color>\w*\s\w*)\sbags?."gm
"""
def parse_rule(rule):
    rule_parts = rule.split('bags contain')
    key = rule_parts[0].strip()
    value_parts = rule_parts[1].strip().split(',')

    values = {}
    for value in value_parts:
        value_trim = value.strip().replace('bags', '').replace('bag', '').replace('.', '').strip()
        if value_trim == 'no other':
            continue
        values[value_trim[2:]] = int(value_trim[0])
    return key, values

print(get_count_of_bag_colors_holding_shiny_gold_bags())

#INCOMPLETE PART TWO
def get_count_of_bags_shiny_gold_bags_hold():
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, 'input_sample.txt')
    rules_dict = build_rules_dict_from_input_file(input_file)
    print(rules_dict)

def get_total_bag_count_inside_shiny_gold_bag(rules_dict):
    return False

def find_interior_bag_counts(rules_dict):
    bag_counts = {1: ['shiny gold']}
    for bag in rules_dict['shiny gold']:
        count = rules_dict['shiny gold'][bag]
        if count in bag_counts.keys():
            bag_counts[count].append(rules_dict['shiny gold'][bag])
        else:
            bag_counts[count] = [rules_dict['shiny gold'][bag]]
    return False

#print(get_count_of_bags_shiny_gold_bags_hold())