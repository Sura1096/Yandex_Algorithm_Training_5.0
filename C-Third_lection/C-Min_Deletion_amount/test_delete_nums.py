import unittest
import min_deletion_amount


class TestDeleteNums(unittest.TestCase):
    def test_min_deletion_amount(self):
        amount = 5
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(
            min_deletion_amount.min_deletion_amount(amount, nums),
            3
        )

        amount = 10
        nums = [1, 1, 2, 3, 5, 5, 2, 2, 1, 5]
        self.assertEqual(
            min_deletion_amount.min_deletion_amount(amount, nums),
            4
        )

        amount = 8
        nums = [5, 3, 10, 9, 4, 11, 7, 8]
        self.assertEqual(
            min_deletion_amount.min_deletion_amount(amount, nums),
            6
        )

        amount = "8"
        nums = [5, 3, 10, 9, 4, 11, 7, 8]
        self.assertEqual(
            min_deletion_amount.min_deletion_amount(amount, nums),
            6
        )


if __name__ == '__main__':
    unittest.main()