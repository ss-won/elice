from wordcloud import WordCloud
from count import count_word_freq
from elice_utils import EliceUtils
elice_utils = EliceUtils()


def create_word_cloud(data):
    counter = count_word_freq(data)

    cloud = WordCloud(font_path='NanumBarunGothic.ttf',
                      background_color='white')
    cloud.fit_words(counter)
    cloud.to_file('cloud.png')
    elice_utils.send_image('cloud.png')


if __name__ == "__main__":
    create_word_cloud(data)
