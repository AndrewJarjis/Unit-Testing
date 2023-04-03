import unittest
from poker import check_straight, check_3ofa_kind, check_royal_flush, play_cards


class TestPoker(unittest.TestCase):

    def test_check_straight(self):
        self.assertEqual(check_straight('S10', 'SJ', 'SQ'), 12)
        self.assertEqual(check_straight('S9', 'S10', 'SJ'), 11)
        self.assertEqual(check_straight('SA', 'SK', 'SQ'), 14)

    def test_check_3ofa_kind(self):
        self.assertEqual(check_3ofa_kind('SA', 'SK', 'SQ'), 14)
        self.assertEqual(check_3ofa_kind('S2', 'S2', 'S2'), 2)
        self.assertEqual(check_3ofa_kind('S2', 'S3', 'S4'), 14)

    def test_check_royal_flush(self):
        self.assertEqual(check_royal_flush('SA', 'SK', 'SQ'), 14)
        self.assertEqual(check_royal_flush('S10', 'SJ', 'SQ'), 0)
        self.assertEqual(check_royal_flush('SA', 'SK', 'S2'), 0)

    def test_play_cards(self):
        self.assertEqual(play_cards('S2', 'S3', 'S4', 'S5', 'S6', 'S7'), 0)
        self.assertEqual(play_cards('SA', 'SK', 'SQ', 'S2', 'S3', 'S4'), 1)
        self.assertEqual(play_cards('S2', 'S3', 'S4', 'SA', 'SK', 'SQ'), -1)


if __name__ == '__main__':
    unittest.main()
