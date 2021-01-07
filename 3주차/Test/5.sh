# Git 명령을 채점하기 위한 편집창입니다.
# 문제를 풀기 위해 필요한 명령을 아래에 입력하세요.
# 여러 개의 명령은 한 줄에 하나씩 입력하세요.
cd soccer-leagues/
git add .
git commit -m "resolve conflict, merge to master"

git checkout master
git merge bugfix/spaces-before-name