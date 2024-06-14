import unittest
import anagram


class TestAnagram(unittest.TestCase):
    def test_is_anagram(self):
        self.assertEqual(
            anagram.is_anagram('dusty', 'study'),
            'YES'
        )

        self.assertEqual(
            anagram.is_anagram('race', 'care'),
            'YES'
        )

        self.assertEqual(
            anagram.is_anagram('part', 'trap'),
            'YES'
        )

        self.assertEqual(
            anagram.is_anagram('race', 'care'),
            'YES'
        )

        self.assertEqual(
            anagram.is_anagram(' ', ' '),
            'YES'
        )

    def test_is_not_anagram(self):
        self.assertEqual(
            anagram.is_anagram('rat', 'bat'),
            'NO'
        )

        self.assertEqual(
            anagram.is_anagram('map', 'mac'),
            'NO'
        )

        self.assertEqual(
            anagram.is_anagram('mississippi', 'miss'),
            'NO'
        )

        self.assertEqual(
            anagram.is_anagram('', 'miss'),
            'NO'
        )
        self.assertEqual(
            anagram.is_anagram('', ' '),
            'NO'
        )


if __name__ == '__main__':
    unittest.main()