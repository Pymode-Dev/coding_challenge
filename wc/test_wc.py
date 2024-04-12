#!/usr/bin/env python3

import unittest

from wc import wc_byte, wc_all, wc_line, wc_word, wc_char


class TestWc(unittest.TestCase):
    def test_all_word_count(self):
        self.assertEqual(wc_byte("test.txt"), 342190)
        self.assertEqual(wc_line("test.txt"), 7145)
        self.assertEqual(wc_word("test.txt"), 58164)
        self.assertEqual(wc_char("test.txt"), 339292)
        self.assertEqual(wc_all("test.txt"), "7145 58164 342190 test.txt")