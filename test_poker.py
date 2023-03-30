import unittest
from poker import check_straight, check_3ofa_kind, check_royal_flush, play_cards


class TestPoker(unittest.TestCase):

    def check_straight(card1, card2, card3):
        cards = [card1, card2, card3]
        values = []
        for card in cards:
            if card[1:] == 'A':
                values.append(1)
                values.append(14)
            else:
                values.append(int(card[1:]))

    def check_3ofa_kind(card1, card2, card3):
        face_cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4,
                      '3': 3,
                      '2': 2}
        cards = [card1, card2, card3]
        values = [face_cards.get(card[1:], int(card[1:])) for card in cards]

    def test_check_royal_flush(self):
        self.assertEqual(check_royal_flush('SA', 'SK', 'SQ'), 14)
        self.assertEqual(check_royal_flush('S10', 'SJ', 'SQ'), 0)
        self.assertEqual(check_royal_flush('SA', 'SK', 'S2'), 0)

    def test_play_cards(self):
        def test_play_cards(self):
            self.assertEqual(play_cards('S2', 'S3', 'S4', 'S5', 'S6', 'S7'), 0)


if __name__ == '__main__':
    unittest.main()
