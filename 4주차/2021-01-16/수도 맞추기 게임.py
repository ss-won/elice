import random
from crawling import getCapitals


def playGame(countryAndCapitals):
    appeared = []

    t = int(input("시도하실 횟수를 입력하세요. \n  > "))
    win = 0
    country = list(countryAndCapitals.keys())

    for i in range(1, t+1):
        while True:
            r = random.randrange(0, len(country))
            q = country[r]
            if not q in appeared:
                appeared.append(q)
                break
        a = countryAndCapitals[q]

        print(f"{i}번째 문제")
        print(f"{q}의 수도는?")

        s = input()

        if s in a:
            print("정답입니다! \n")
            win += 1
        else:
            print(f"오답입니다. 정답은 {', '.join(a)} 입니다.\n")

    print("="*20)
    print(f"당신의 점수 : {win}/{t}")


def main():
    countryAndCapitals = getCapitals()
    playGame(countryAndCapitals)


if __name__ == "__main__":
    main()
