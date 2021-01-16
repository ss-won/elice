import random
from crawling import getCapitals


def playGame(countryAndCapitals):
    appeared = []

    t = int(input("시도하실 횟수를 입력하세요. \n  > "))
    win = 0
    country = list(countryAndCapitals.keys())

    for i in range(1, t+1):
        questions = [""]*4
        answers = [""]*4
        answerNum = random.randrange(1, 5)

        for j in range(4):
            while True:
                r = random.randrange(0, len(country))
                q = country[r]
                a = countryAndCapitals[q]
                if (j == answerNum-1 and q in appeared) or q in questions:
                    continue
                else:
                    questions[j] = q
                    answers[j] = a
                    appeared.append(q)
                    break

        print(f"{i}번째 문제")
        print(f"{questions[answerNum-1]}의 수도로 올바른 것은?")
        for i in range(4):
            print(f"{i+1}: {', '.join(answers[i])}")

        # 정답 입력이 인덱스와 관계없는 것이 주어지면 안되므로 예외처리를 한다.
        while True:
            try:
                print("정답을 입력하세요.")
                s = int(input(" >"))
                if s < 1 or s > 4:
                    print("1~4 사이의 값을 입력하세요.")
                else:
                    break
            except Exception:
                print("1~4 사이의 값을 입력하세요.")

        if s == answerNum:
            print("정답입니다! \n")
            win += 1
        else:
            print(f"오답입니다. 정답은 {', '.join(answers[answerNum-1])} 입니다.\n")

    print("="*20)
    print(f"당신의 점수 : {win}/{t}")


def main():
    countryAndCapitals = getCapitals()
    playGame(countryAndCapitals)


if __name__ == "__main__":
    main()
