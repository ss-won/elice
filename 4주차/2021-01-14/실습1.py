import re

text = "hello, elice!"

# p1은 pattern 1의 의미입니다! 정규표현식을 입력해보세요. (ex. "e", "elice")
p1 = ""

m1 = re.findall(p1, text)   # text 문자열 변수에서 정규식 p1로 매칭한 결과를 나타냅니다.

print(m1)
