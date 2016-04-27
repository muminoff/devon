#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_devon
----------------------------------

Tests for `devon` module.
"""

import unittest

from devon.devon import WordProcessor


class TestWordProcessor(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_segmentize(self):
        self.assertEqual(
            WordProcessor.segmentize(word='sardor'), ('sar', 'dor'))


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
