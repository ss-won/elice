
# 읽기 모드로 words.txt 파일을 open 함수를 통해 열고, 변수 f에 연결하세요.
f = open("words.txt", mode="r")

# 변수 lines에 f의 데이터를 문자열 형태로 읽어오세요.
lines = f.read()

# 변수 lines의 데이터를 개행문자를 기준으로 나눈 원소들을 가진 리스트 lines로 다시 만드세요.
lines = lines.split("\n")

# 리스트 lines의 모든 원소를 반복문을 활용하여 하나하나 출력해주세요.
for word in lines:
    print(word)
