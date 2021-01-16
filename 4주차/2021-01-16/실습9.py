from wordcloud import WordCloud
from wordcloud import STOPWORDS
from count import count_word_freq
from text import data

from elice_utils import EliceUtils
elice_utils = EliceUtils()


def create_word_cloud(data):
    counter = count_word_freq(data)
    # 코드를 작성하세요.
    # stopwords : 불의어 제거

    cloud = WordCloud(background_color='white', stopwords=STOPWORDS)
    cloud.fit_words(counter)
    cloud.to_file('cloud.png')


if __name__ == "__main__":
    create_word_cloud(data)
