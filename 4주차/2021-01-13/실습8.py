import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from elice_utils import EliceUtils
elice_utils = EliceUtils()

font = fm.FontProperties(fname='./NanumBarunGothic.ttf')

x = range(31)
temperatures = [
    22.8, 25.3, 32.6, 31.8, 29.0, 27.1, 29.2,
    28.1, 24.2, 26.5, 29.5, 28.2, 30.9, 31.9,
    33.2, 34.0, 32.1, 33.2, 34.1, 34.7, 36.9,
    38.0, 35.7, 36.8, 34.1, 33.7, 35.4, 35.2,
    36.7, 36.9, 38.3
]

# 막대 그래프를 그립니다.
plt.bar(x, temperatures)

# 그래프의 제목을 설정합니다. 제목은 상단 중앙에 생성됩니다.
plt.title('2018년 7월 서울 최고기온', fontproperties=font)

# 그래프의 x축에 들어갈 tick 텍스트를 설정해 줍니다.
plt.xticks(x, [f'7월 {i+1}일' for i in range(31)],
           fontproperties=font, rotation="vertical")

# 엘리스 화면에 그래프를 표시합니다.
plt.savefig('graph.png')
elice_utils.send_image('graph.png')
