from collections import Counter
from string import punctuation


def count_word_freq(data):
    _data = data.lower()

    for p in punctuation:
        _data = _data.replace(p, "")

    _data = _data.split()

    counter = Counter(_data)

    return counter
