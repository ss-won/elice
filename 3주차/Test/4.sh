# Git 명령을 채점하기 위한 편집창입니다.
# 문제를 풀기 위해 필요한 명령을 아래에 입력하세요.
# 여러 개의 명령은 한 줄에 하나씩 입력하세요.
cd food_list
git branch food/cost
git branch food/feedback

git checkout food/cost
git add food_cost.txt
git commit -m "add food_cost.txt"

git checkout food/feedback
git add food_feedback.txt
git commit -m "add food_feedback.txt"