#!/usr/bin/env python
# -*- coding:utf-8 -*-

from kmp import is_sub
import unittest
from data_str import DATA_LONG_STR

class TestKMP(unittest.TestCase):
    def setUp(self):
        self.list_normal_short = ["abcdabd", "abc"]
        self.list_normal_long = [DATA_LONG_STR, "abcdabd"]
        self.list_special_characters = ["@abcd\taaaaaaaabcde", "abcde"]
        self.list_not_match = ["aaaa aaaaaaa aaaaa", "abc"]
        self.list_space_first = ["   abc abcd abcde","abcde"]


    def tearDown(self):
        pass

    def test_normal_short(self):
        isMatch = is_sub(self.list_normal_short[0], self.list_normal_short[1])
        self.assertTrue(isMatch)    
    
    def test_normal_long(self):
        isMatch = is_sub(self.list_normal_long[0], self.list_normal_long[1])
        self.assertTrue(isMatch)

    def test_special_characters(self):
        isMatch = is_sub(self.list_special_characters[0], self.list_special_characters[1])
        self.assertTrue(isMatch)

    def test_not_match(self):
        isMatch = is_sub(self.list_not_match[0], self.list_not_match[1])
        self.assertFalse(isMatch)

    def test_space_first(self):
        isMatch = is_sub(self.list_space_first[0], self.list_space_first[1])
        self.assertTrue(isMatch)


if __name__ == '__main__':
    unittest.main()
