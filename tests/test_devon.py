#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_devon
----------------------------------

Tests for `devon` module.
"""

import unittest

from devon.devon import WordProcessor, FSMStemmer


class TestWordProcessor(unittest.TestCase):

    def setUp(self):
        self.corpora_lat = """
        Barcha insonlar erkin, qadr-qimmat va huquqlarda tang bo‘lib tug‘iladilar. Ular aql va vijdon sohibidirlar va bir-birlariga birodarlarcha muomala qilishlari zarur.
        """  # noqa
        self.corpora_cyr = """
        Барча инсонлар эркин, қадр-қиммат ва ҳуқуқларда танг бўлиб туғиладилар. Улар ақл ва виждон соҳибидирлар ва бир-бирларига биродарларча муомала қилишлари зарур.
        """  # noqa

    def tearDown(self):
        del self.corpora_lat
        del self.corpora_cyr

    def test_stem(self):
        stemmer = FSMStemmer()
        stems = stemmer.stem(words=self.corpora_lat, multi_words=True)
        expectation = [
                'Barcha', 'inson', 'erkin,', 'qadr-qimmat', 'va',
                'huquq', 'ta', 'bo‘lib', 'tug‘iladilar.', 'U', 'aql',
                'va', 'vijdon', 'sohibidir', 'va', 'bir-bir',
                'birodarlarcha', 'muomala', 'qilish', 'zarur.']
        self.assertEqual(stems, expectation)

    def test_segmentize(self):
        self.assertEqual(
            WordProcessor.segmentize(word='sardor'), ('sar', 'dor'))

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
