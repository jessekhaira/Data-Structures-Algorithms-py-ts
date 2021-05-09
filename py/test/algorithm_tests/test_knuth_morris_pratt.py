""" This module contains tests for the Knuth-Morris-Pratt algorithm """
from py.algorithms.knuth_morris_pratt import knuth_morris_pratt
import unittest


class KnuthMorrisPrattTests(unittest.TestCase):

    def test1(self):
        bigstr = ""
        substr = "xp"
        self.assertEqual(knuth_morris_pratt(bigstr, substr), -1)

    def test2(self):
        bigstr = "xp"
        substr = ""
        self.assertEqual(knuth_morris_pratt(bigstr, substr), -1)

    def test3(self):
        bigstr = "loepanajsdnqjkweqwhekjdhfasdkjlashdlasjdjksaasdjias"
        substr = "weqwhek"
        self.assertEqual(knuth_morris_pratt(bigstr, substr), 14)

    def test4(self):
        bigstr = "bizxcnjasd"
        substr = "sd"
        self.assertEqual(knuth_morris_pratt(bigstr, substr), 8)

    def test5(self):
        bigstr = "sd"
        substr = "sd"
        self.assertEqual(knuth_morris_pratt(bigstr, substr), 0)


if __name__ == "__main__":
    unittest.main()