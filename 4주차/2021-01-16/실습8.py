from collections import Counter
from string import punctuation
from text import data


def count_word_freq(data):
    # 전처리: 특수문자 대소문자 구분 없애주기
    _data = data.lower()
    # 전처리: 특수문자 지워주기
    for p in punctuation:
        _data = _data.replace(p, "")

    _data = _data.split()
    counter = Counter(_data)
    return counter


if __name__ == "__main__":
    print(count_word_freq(data))
