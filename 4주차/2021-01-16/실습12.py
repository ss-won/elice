from mecab import MeCab
mecab = MeCab()


text = "광화문역 주변에 있는 맛집을 알고 싶어요. 정보를 얻을 수 있을까요?"

# 1. 형태소 별로 나눠 출력해보기
print("형태소 별로 나눠 출력")
print("======================")
for word in mecab.morphs(text):
    print(word)

print("\n")
print("형태소 별로 나눠 명사만 출력")
print("======================")
# 2. 명사만 출력해보기
for word in mecab.nouns(text):
    print(word)

print("\n")
print("형태소 별로 나눠 품사와 함께 출력")
print("======================")
# 3. 형태소 별로 나누고 품사 출력해보기
for word in mecab.pos(text):
    print(word)
