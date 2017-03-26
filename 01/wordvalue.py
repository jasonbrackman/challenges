import collections
import functools
from data import DICTIONARY, LETTER_SCORES


@functools.lru_cache()
def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'rt') as handle:
        return [word.strip() for word in handle.readlines()]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    letters = collections.Counter(word.upper())
    total = sum(LETTER_SCORES[letter] * count for letter, count in letters.items() if letter in LETTER_SCORES)
    return total


def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    kv = {word: calc_word_value(word) for word in words}
    k, v = max(kv.items(), key=lambda x: x[1])
    return k

if __name__ == "__main__":
    pass
