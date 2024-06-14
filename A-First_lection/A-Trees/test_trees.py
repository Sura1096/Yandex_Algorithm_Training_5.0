import unittest
from trees import tree_amount


class TestTrees(unittest.TestCase):
    def test_positive_tree_amount(self):
        self.assertEqual(
            tree_amount(0, 0, 0, 0),
            1
        )

        self.assertEqual(
            tree_amount(0, 7, 12, 5),
            25
        )

        self.assertEqual(
            tree_amount(4, 5, 12, 9),
            23
        )

        self.assertEqual(
            tree_amount(78, 4, 6, 10),
            30
        )

        self.assertEqual(
            tree_amount(3144164, 53670532, 29082204, 57704543),
            137313116
        )
        self.assertEqual(
            tree_amount(13857372, 5986960, 10033886, 33459235),
            66918471
        )

        self.assertEqual(
            tree_amount(39719203, 54264550, 20794499, 7324191),
            108529101
        )

        self.assertEqual(
            tree_amount(409, 981, 431, 932),
            1963
        )
        self.assertEqual(
            tree_amount(527, 284, 270, 864),
            1729
        )

    def test_negative_tree_amount(self):
        self.assertEqual(
            tree_amount(-55848766, 34773569, 30211467, 86943283),
            207777086
        )

        self.assertEqual(
            tree_amount(-76494637, 19846840, -84830300, 77907030),
            155814061
        )
        self.assertEqual(
            tree_amount(-54097964, 782462, -4866258, 70956351),
            141912703
        )

        self.assertEqual(
            tree_amount(17650374, 57638592, -33309862, 98987671),
            207586500
        )


if __name__ == '__main__':
    unittest.main()