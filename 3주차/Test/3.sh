# Git 명령을 채점하기 위한 편집창입니다.
# 문제를 풀기 위해 필요한 명령을 아래에 입력하세요.
# 여러 개의 명령은 한 줄에 하나씩 입력하세요.
cd random_quotes

git reset HEAD
git add quotes/politics.txt quotes/science.txt
git commit -m "first commit"

git add *
git commit -m "second commit"