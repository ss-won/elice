import re

# 아래 p1, p2에 직접 정규표현식을 입력해보세요.

p1 = "Life"     # Life 포함하면 매치
p2 = "is"       # is 포함하면 매치

m1 = re.findall(p1, "Life is short")
m2 = re.findall(p2, "Life is short")

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)
