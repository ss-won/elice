-- 아래에 미션을 수행하는 코드를 작성해 봅시다.
--- where절 먼저 실행되고 -> select절이 실행됨
SELECT *, (weight/(height*height/10000)) AS bmi from student;
SELECT *, (weight/(height*height/10000)) AS bmi from student
WHERE (weight/(height*height/10000)) < 18.5 or (weight/(height*height/10000)) > 25.0;