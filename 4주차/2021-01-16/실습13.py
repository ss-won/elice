from collections import Counter
from string import punctuation
import mecab
mecab = mecab.MeCab()


def count_word_freq(data):
    _data = data.lower()

    for p in punctuation:
        _data = _data.replace(p, "")

    # 명사를 추출하세요.
    _data = mecab.nouns(_data)

    counter = Counter(_data)

    return counter
