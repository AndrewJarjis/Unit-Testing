cards = ('S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA')


def check_straight(card1, card2, card3):
    cards = [card1, card2, card3]
    values = []
    for card in cards:
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
    face_cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11}
    cards = [card1, card2, card3]
    values = [face_cards.get(card[1:], int(card[1:])) for card in cards]
    if len(set(values)) == 1:
        return values[0]
    else:
        return 0


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
        return -1
    elif left_rank < right_rank:
        return 1
    else:
        return 0


def get_rank(cards):
    cards.sort()
    values = [int(card[1:]) for card in cards]
    if len(set(values)) == 1:
        return 3
    straight_value = check_straight(*cards)
    if straight_value:
        if straight_value == 14:
            return 5
        return 4
    return 1
