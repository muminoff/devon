# -*- coding: utf-8 -*-


class WordProcessor(object):

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def segmentize(word):
        vowels = ('a','e','u','i','o')
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
