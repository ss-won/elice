import random

f = open("words.txt", 'r')
WORDS = f.read().split("\n")


def game(last_word, player_name):
    word = input(f"[{player_name}] 단어 입력 : ")
    
    # 패배 조건 1
    if last_word[-1] != word[0]:
        print(f"[{player_name}] 패배했습니다.")
        print("이유 : 상대방이 말한 단어의 마지막 알파벳으로 시작하지 않습니다.")
        return None
    # 패배 조건 2
    if not word in WORDS:
        print(f"[{player_name}] 패배했습니다.")
        print("이유 : 존재 하지 않는 단어입니다.")
        return None
    return word


def main() :
    players = ["player 1", "player 2"]

    last_word = WORDS[random.randint(0, len(WORDS))]
    
    print("시작 단어 :", last_word)
    i = 0
    while True:
        last_word = game(last_word, players[i])
        if last_word == None:
            break
        i = (i+1)%2

# __name__은 함수의 명칭을 뜻하는 것으로 파일에서 main 함수만 실행하겠다는 뜻입니다.
if __name__ == "__main__" :
    main()