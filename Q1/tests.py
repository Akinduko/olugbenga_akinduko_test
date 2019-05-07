import unittest
from Q1 import check_overlap


class TestsForcheck_overlap(unittest.TestCase):

    # Test methods for check_overlap Function of two lines on x-axis

    def test_PositiveInt_check_overlap(self):
        result = check_overlap((1, 5), (3, 6))
        self.assertEqual(result, True)

    def test_PositiveInt_Notcheck_overlap(self):
        result = check_overlap((1, 5), (6, 11))
        self.assertEqual(result, False)

    def test_NegativeInt_check_overlap(self):
        result = check_overlap((-1, -5), (-3, -6))
        self.assertEqual(result,True)

    def test_NegativeInt_Notcheck_overlap(self):
        result = check_overlap((-1, -5), (-6, -11))
        self.assertEqual(result, False)

    def test_Integers_check_overlap(self):
        result = check_overlap((-1, 2), (0, -2))
        self.assertEqual(result, True)

    def test_Origin_check_overlap(self):
        result = check_overlap((0, 0), (0, 0))
        self.assertEqual(result, True)

    def test_Integers_check_overlaps(self):
        result = check_overlap((-1, -3), (1, 3))
        self.assertEqual(result, False)


unittest.main()