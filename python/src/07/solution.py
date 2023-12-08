"""https://adventofcode.com/2023/day/7"""

import pathlib


def solve(file_name, get_type_func, strengths):
    all_hands = categorize_hands(file_name, get_type_func, strengths)
    return calculate_total_winnings(all_hands)


def categorize_hands(file_name, get_type_func, strengths):
    all_hands = {'high': {}, 'one': {}, 'two': {}, 'three': {},
        'full': {}, 'four': {}, 'five': {},}
    input_file = pathlib.PurePath(pathlib.Path(__file__).parent, file_name)
    with open(input_file) as file:
        while True:
            line = file.readline().replace('\n', '')
            if not line:
                break
            hand_type, converted_hand, bid = process_line(line, get_type_func, strengths)
            all_hands[hand_type][converted_hand] = bid
    return all_hands

def process_line(line, get_type_func, strengths):
    [hand, bid] = line.split(' ')
    hand_type = get_type_func(hand)
    converted_hand = convert_hand(strengths, hand)
    return hand_type, converted_hand, int(bid)


def get_type_of_hand(hand):
    len_to_type = {1: 'five', 4: 'one', 5: 'high'}
    card_count = len(set(hand))
    if card_count == 2:
        freq = hand.count(hand[0])
        return 'four' if freq in [1,4] else 'full'
    elif card_count == 3:
        freq = hand.count(hand[0])
        if freq == 3:
            return 'three'
        elif freq == 2:
            return 'two'
        else:
            freq = hand.count(hand[1])
            return 'two' if freq == 2 else 'three'
    else:
        return len_to_type[card_count]

def get_type_of_hand_with_jokers(hand):
    JOKER = 'J'
    card_count = len(set(hand))
    if card_count == 1:
        return 'five'
    elif card_count == 2:
        if JOKER in hand:
            return 'five'
        freq = hand.count(hand[0])
        return 'four' if freq in [1,4] else 'full'
    elif card_count == 3:
        if JOKER in hand:
            return 'four'
        freq = hand.count(hand[0])
        if freq == 3:
            return 'three'
        elif freq == 2:
            return 'two'
        else:
            freq = hand.count(hand[1])
            return 'two' if freq == 2 else 'three'
    elif card_count == 4:
        return 'three' if JOKER in hand else 'one'
    elif card_count == 5:
        return 'two' if JOKER in hand else 'high'
    return False

# So sorting will be easier later
def convert_hand(strengths, hand):
    converted_hand = ''
    for char in hand:
        converted_hand += strengths[char]
    return converted_hand


def calculate_total_winnings(all_hands):
    winnings_per_bucket = []
    min_rank = 0
    for bucket in all_hands.keys():
        winnings, updated_min_rank = calculate_winnings_for_bucket(all_hands[bucket], min_rank)
        winnings_per_bucket.append(winnings)
        min_rank = updated_min_rank
    return sum(winnings_per_bucket)


def calculate_winnings_for_bucket(bucket, min_rank):
    winnings = 0
    if len(bucket) == 0:
        return winnings, min_rank

    hands = list(bucket.keys())
    hands.sort(reverse=True)

    for index, hand in enumerate(hands):
        updated_rank = index + 1 + min_rank
        winnings += bucket[hand] * updated_rank
    
    return winnings, updated_rank


strengths = {
    '2': 'M', '3': 'L', '4': 'K', '5': 'J', '6': 'I', '7': 'H', '8': 'G',
    '9': 'F', 'T': 'E', 'J': 'D', 'Q': 'C', 'K': 'B', 'A': 'A'
}

joker_strengths = {
    'J': 'N', '2': 'M', '3': 'L', '4': 'K', '5': 'J', '6': 'I', '7': 'H', 
    '8': 'G', '9': 'F', 'T': 'E', 'Q': 'C', 'K': 'B', 'A': 'A'
}

#print(solve('input.txt', get_type_of_hand, strengths))
#print(solve('input_sample.txt', get_type_of_hand_with_jokers, joker_strengths)) # 250888594 too high, but works for sample