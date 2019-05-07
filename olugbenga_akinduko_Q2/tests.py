
import unittest
from olugbenga_akinduko_Q2 import compare_string


class TestsForStrings(unittest.TestCase):

    # -------------------TESTS for Greater Function-----------------------
    def test1_for_greater(self):
        strings = compare_string('1.1', '1.3')
        self.assertEqual(strings.greater(), '1.3 is greater than 1.1')

    def test2_for_greater(self):
        strings = compare_string('-1.1', '-1.3')
        self.assertNotEqual(strings.greater(), '-1.3 is greater than -1.1')

    def test3_for_greater(self):
        strings = compare_string('1.1', '0')
        self.assertTrue(strings.greater(), '1.1 is greater than 0')

    # -------------------TESTS for Lesser Function-------------------------
    def test1_for_lesser(self):
        strings = compare_string('1.1', '1.3')
        self.assertEqual(strings.lesser(), '1.1 is lesser than 1.3')

    def test2_for_lesser(self):
        strings = compare_string('-1.1', '-1.3')
        self.assertNotEqual(strings.lesser(), '-1.1 is lesser than -1.3')

    def test3_for_lesser(self):
        strings = compare_string('1.1', '0')
        self.assertTrue(strings.lesser(), '0 is lesser than 1.1')

    # ------------TESTS for Equal Function-----------------------------
    def test1_for_equal(self):
        strings = compare_string('1.1', '1.3')
        self.assertEqual(strings.equal(), '1.3 is not equal to 1.1')

    def test2_for_equal(self):
        strings = compare_string('1.1', '1.1')
        self.assertEqual(strings.equal(), '1.1 is equal to 1.1')

    def test3_ForNotEqual(self):
        strings = compare_string('1.1', '1.3')
        self.assertNotEqual(strings.equal(), '1.1 not equal 1.3')

unittest.main()

