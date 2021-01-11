-- 아래에 쿼리를 작성해 보세요.
SELECT room FROM student
GROUP BY room 
HAVING count(room) = 1;
