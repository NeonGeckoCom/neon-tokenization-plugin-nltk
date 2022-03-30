from ovos_plugin_manager.tokenization import Tokenizer
from ovos_plugin_manager.segmentation import Segmenter

from nltk.tokenize import WordPunctTokenizer, sent_tokenize


class NltkTokenizer(Tokenizer):
    def __init__(self, config=None):
        super().__init__(config)
        self.tokenizer = WordPunctTokenizer()

    def tokenize(self, text, lang=None):
        return self.tokenizer.tokenize(text)

    def span_tokenize(self, text, lang=None):
        spans = zip(self.tokenizer.span_tokenize(text),
                    self.tokenizer.tokenize(text))
        return [(s[0][0], s[0][1], s[1]) for s in spans]


class NltkSegmenter(Segmenter):
    def segment(self, text):
        return sent_tokenize(text)

