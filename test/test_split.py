import unittest

from neon_tokenization_plugin_nltk import NltkTokenizer


class TestNltkTokenizer(unittest.TestCase):

    def test_tokenize(self):
        solver = NltkTokenizer()
        self.assertEqual(solver.tokenize(
            "This is a test. This is another test"),
            ['This', 'is', 'a', 'test', '.', 'This', 'is', 'another', 'test'])

    def test_spans(self):
        solver = NltkTokenizer()
        self.assertEqual(solver.span_tokenize(
            "This is a test. This is another test"),
            [(0, 4, 'This'),
             (5, 7, 'is'),
             (8, 9, 'a'),
             (10, 14, 'test'),
             (14, 15, '.'),
             (16, 20, 'This'),
             (21, 23, 'is'),
             (24, 31, 'another'),
             (32, 36, 'test')])
