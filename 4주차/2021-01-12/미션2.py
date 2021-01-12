### 완성 코드를 시연해보세요!

import random

words = set()
saidWord = set()


def loadWord() :
    # word.txt 를 불러오는 함수입니다.
    f = open("words.txt", mode="r")
    lines = f.read().split("\n")
    for line in lines:
        words.add(line)

def randWord():
    # 랜덤 단어를 선택하는 함수입니다.
    word = list(words)[random.randint(0, len(words))]
    return word

def isWord(word): 
    # word 집합에 들어있는 단어인지 확인하는 함수입니다.
    return word in words

def game(lastWord):
    # 사용자가 게임을 진행하는 함수입니다. 
    # 사용자에게 단어를 입력받고, 패배인지 아닌지 확인하는 로직을 넣어주세요.
    word = input("단어 입력 : ")
    # 패배 조건 1
    if lastWord[-1] != word[0]:
        print("패배했습니다.")
        print("이유 : 상대방이 말한 단어의 마지막 알파벳으로 시작하지 않습니다.")
        return None
    # 패배 조건 2
    if not isWord(word):
        print("패배했습니다.")
        print("이유 : 존재 하지 않는 단어입니다.")
        return None
    # 패배 조건 3
    # 이미 사용했던 단어가 나오는 경우 패배합니다.
    if word in saidWord:
        print("패배했습니다.")
        print("이유 : 기존에 나온 단어들 중 하나와 중복되는 단어를 말했습니다.")
        return None
    saidWord.add(word)
    return word
    
def cpuGame(last_word):
    # 컴퓨터가 게임을 진행하는 함수입니다.
    # word 집합에서 아직 안 쓰인 단어를 필터링하고, 랜덤으로 하나의 단어를 선택해서 리턴해주세요.
    fwords = [x for x in words if not x in saidWord and x[0] == last_word[-1]]
    word = fwords[random.randint(0,len(fwords))]
    saidWord.add(word)
    print("CPU :", word)
    return word
    
def main():
    # 전체 함수를 활용한 main 함수를 구현해보세요.
    loadWord()
    last_word = randWord()
    print("CPU :", last_word)
    
    i = 0
    while last_word != None:
        if i == 0:
            last_word = game(last_word)
            i = (i+1)%2
        else:
            word = last_word = cpuGame(last_word)
            i = (i+1)%2
        
if __name__ == "__main__" :
    main()