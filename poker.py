cards = {'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10, 'SJ': 11, 'SQ': 12,
         'SK': 13, 'SA': 14}


def check_straight(card1, card2, card3):
    current_cards = [card1, card2, card3]
    values = []
    for card in current_cards:
        if card[1:] == 'T':
            values.append(10)
        elif card[1:] == 'J':
            values.append(11)
        elif card[1:] == 'Q':
            values.append(12)
        elif card[1:] == 'K':
            values.append(13)
        elif card[1:] == 'A':
            values.append(14)
        else:
            values.append(int(card[1:]))
    values.sort()
    if values[0] == values[1] - 1 and values[1] == values[2] - 1:
        return values[2]
    else:
        return 0

def check_3ofa_kind(card1, card2, card3):
    current_cards = [card1, card2, card3]
    face_values = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    values = []
    for card in current_cards:
        if card[1:] in face_values:
            values.append(face_values[card[1:]])
        else:
            values.append(int(card[1:]))
    if len(set(values)) == 1:
        return values[0]
    else:
        return 14



def check_royal_flush(card1, card2, card3):
    straight_value = check_straight(card1, card2, card3)
    if straight_value == 14:
        return 14
    return 0


def play_cards(left1, left2, left3, right1, right2, right3):
    left_cards = [left1, left2, left3]
    right_cards = [right1, right2, right3]
    left_rank = get_rank(left_cards)
    right_rank = get_rank(right_cards)
    if left_rank > right_rank:
        return 1
    elif left_rank < right_rank:
        return -1
    else:
        return 0


def get_rank(current_cards):
    current_cards.sort()
    values = [cards[card] for card in current_cards]
    if len(set(values)) == 1:
        return 3
    straight_value = check_straight(*current_cards)
    if straight_value:
        if straight_value == 14:
            return 5
        return 4
    return 1
