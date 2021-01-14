import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "마우스의 가격은 7,000원이고, 모니터의 가격은 72,000원이고, 키보드의 가격은 216,000원이고, 그래픽카드는 1,500,000원입니다."

p1 = "(\d{0,3},)?(\d{3},)*\d{1,3}"          # 금액을 참조하려는 잘못된 정규식 패턴
# 올바른 패턴을 작성해보세요.
p2 = "(?:\d{0,3},)?(?:\d{3},)*(?:\d{1,3})"

m1 = re.findall(p1, text)
m2 = re.findall(p2, text)

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)
