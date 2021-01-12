# 이미 말한 단어가 저장 되는 리스트 입니다.
said_word = []

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
    # 패배 조건 3 - 추가된 조건
    # 이미 사용했던 단어가 나오는 경우 패배합니다.
    if word in said_word:
        print(f"[{player_name}] 패배했습니다.")
        print("이유 : 기존에 나온 단어들 중 하나와 중복되는 단어를 말했습니다.")
        return None
    said_word.append(word)
    return word
    
def main() :
    import random
    global WORDS 
    players = ["player1", "player2"]
    f = open("words.txt", 'r')
    WORDS = f.read().split("\n")
    
    last_word = WORDS[random.randint(0, len(WORDS))]
    print("시작 단어 :", last_word)
    
    i = 0
    
    # 변수 last_word가 None이 반환될 때 까지 game 함수를 호출합니다.
    while last_word != None:
        last_word = game(last_word, players[i])
        i = (i+1)%2
if __name__ == "__main__" :
    main()