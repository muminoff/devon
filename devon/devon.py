# -*- coding: utf-8 -*-
import string
from fysom import Fysom


class FSMStemmer(object):
    """
    Stemmer implementation based on Finite State Machine with Fysom

    """

    events = [
        ('dir', 'start', 'b'), ('dirda', 'start', 'b'),
        ('ku', 'start', 'b'), ('mi', 'start', 'b'),
        ('mikan', 'start', 'b'), ('siz', 'start', 'b'),
        ('day', 'start', 'b'), ('dek', 'start', 'b'),
        ('niki', 'start', 'b'), ('dagi', 'start', 'b'),
        ('mas', 'start', 'd'), ('ning', 'start', 'f'),
        ('lar', 'start', 'g'), ('lar', 'e', 'g'),
        ('dan', 'd', 'e'), ('da', 'd', 'e'),
        ('ga', 'd', 'e'), ('ni', 'd', 'e'),
        ('dan', 'start', 'e'), ('da', 'start', 'e'),
        ('ga', 'start', 'e'), ('ni', 'start', 'e'),
        ('lar', 'f', 'g'), ('miz', 'start', 'h'),
        ('ngiz', 'start', 'h'), ('m', 'start', 'h'),
        ('si', 'start', 'h'), ('i', 'start', 'h'),
        ('ng', 'start', 'h'), ('miz', 'f', 'h'),
        ('ngiz', 'f', 'h'), ('m', 'f', 'h'),
        ('si', 'f', 'h'), ('i', 'f', 'h'),
        ('ng', 'f', 'h'), ('miz', 'e', 'h'),
        ('ngiz', 'e', 'h'), ('m', 'e', 'h'),
        ('si', 'e', 'h'), ('i', 'e', 'h'),
        ('ng', 'e', 'h'), ('lar', 'h', 'g'),
        ('dagi', 'g', 'start')
    ]

    def __init__(self, *args, **kwargs):
        pass

    def stem(self, words, multi_words=False):

        final_stems = list()

        if isinstance(words, str):
            
            if multi_words:
                splitted_words = words.strip().split(" ")
                
                for word in splitted_words:
                    final_stems.append(self.do_stem(word))

                return final_stems

            final_stems.append(self.do_stem(words))
            return final_stems

        elif isinstance(words, list) or isinstance(words, tuple) or \
                isinstance(words, set):

                    for word in words:
                        final_stems.append(self.do_stem(word))

                    return final_stems

        return None

    def do_stem(self, word):
        fsm = Fysom(initial='start', events=self.events)
        # FIXME: uncomment below and make sanitize functions support both Python 2 and 3 versions
        # word = WordProcessor.sanitize(word)
        i = len(word) - 1
        j = len(word)

        while(True):
            if (i<=0):
                break
            v = word[i:j]
            # print v
            res = fsm.can(v)
            if (res):
                if (v == 'i' and fsm.can(word[i-1:j])):
                    i = i - 1
                    continue
                fsm.trigger(v)
                if (fsm.current == 'h'):
                    if (word[i-1:i]=='i'):
                        i = i - 1 #skip i
                        if (word[i-1:i]=='n' ):
                            # ning qushimchasi
                            fsm.current = 'start'
                            continue
                elif (fsm.current == 'b'):
                    fsm.current = 'start'
                j = i

            i =  i - 1

        return word[:j]

class WordProcessor(object):

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def sanitize(word):
        """
        Sanitizing word using `translate()` -- performing raw string operations in C
        with a lookup table - there's not much that will beat that bar writing your own C code.

        Reference http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
        """
        table = str.maketrans("", "")
        return word.translate(table, string.punctuation)


    @staticmethod
    def segmentize(word):
        vowels = {'a','e','u','i','o'}
        word = word.lower()
        segments = list()
        start = -1
        end = 0
        pc = ''
        for c in word:
            if c in vowels:
                if (start > -1):
                    if (end - 2 == start and pc in vowels):
                        end = end + 1
                    segments.append(word[start:end-1])
                    start = end - 1
                else:
                    start = 0	
            end = end + 1
            pc = c
        if (start > -1):
            segments.append(word[start:])
        else:
            raise NotImplementedError

        return tuple(segments)
