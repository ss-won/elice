# 끝말잇기 게임 프로그램을 만들어주세요!
players = ["player1", "player2"]
last_word = input("[player1] 단어 입력 : ")

i = 1
while True:
    # f"[{players[i]}]"에서 {}는 변수가 들어갈 자리를 뜻합니다.
    word = input(f"[{players[i]}] 단어 입력 : ")
    if last_word[-1] != word[0]:
        print(f"[{players[i]}] 패배!")
        break
    last_word = word
    i = (i+1)%2