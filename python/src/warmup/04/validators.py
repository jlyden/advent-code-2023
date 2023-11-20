import re

def evaluate_byr(value):
    value = evaluate_year_string(value)
    if value == False:
        return False
    if 1920 <= value <= 2002:
        return True
    return False

def evaluate_ecl(value):
    valid_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if value in valid_values:
        return True
    return False

def evaluate_eyr(value):
    value = evaluate_year_string(value)
    if value == False:
        return value
    if 2020 <= value <= 2030:
        return True
    return False

def evaluate_hcl(value):
    if len(value) != 7:
        return False
    match = re.search("#[0-9a-f]{6}", value)
    if match == None:
        return False
    return True

def evaluate_hgt(value):
    unit = value[-2:]
    if unit not in ['cm', 'in']:
        return False
    measurement = value.replace(unit, '')
    try:
        measurement = int(measurement)
    except ValueError:
        return False
    else:
        match unit:
            case 'cm':
                if 150 <= measurement <= 193:
                    return True
            case 'in':
                if 59 <= measurement <= 76:
                    return True
        return False

def evaluate_iyr(value):
    value = evaluate_year_string(value)
    if value == False:
        return value
    if 2010 <= value <= 2020:
        return True
    return False

def evaluate_pid(value):
    if len(value) != 9:
        return False
    try:
        value = int(value)
    except ValueError:
        return False
    else:
        return True

def evaluate_year_string(value):
    if len(value) != 4:
        return False
    try:
        value = int(value)
    except ValueError:
        return False
    else:
        return value
