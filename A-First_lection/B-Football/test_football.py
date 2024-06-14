import unittest
from football import ball_amount


class TestBallAmount(unittest.TestCase):
    def test_ball_amount(self):
        self.assertEqual(
            ball_amount(0, 0, 0, 0, 1),
            1
        )

        self.assertEqual(
            ball_amount(0, 2, 0, 3, 1),
            5
        )

        self.assertEqual(
            ball_amount(0, 2, 0, 3, 2),
            6
        )

        self.assertEqual(
            ball_amount(0, 1, 3, 4, 2),
            3
        )

        self.assertEqual(
            ball_amount(0, 0, 1, 2, 1),
            1
        )

        self.assertEqual(
            ball_amount(4, 3, 3, 4, 1),
            1
        )

        self.assertEqual(
            ball_amount(2, 5, 1, 5, 1),
            7
        )

        self.assertEqual(
            ball_amount(2, 3, 4, 0, 1),
            0
        )

        self.assertEqual(
            ball_amount(2, 5, 0, 4, 2),
            8
        )

        self.assertEqual(
            ball_amount(5, 0, 3, 4, 1),
            0
        )


if __name__ == '__main__':
    unittest.main()