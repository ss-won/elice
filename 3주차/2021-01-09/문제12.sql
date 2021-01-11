-- 아래에 쿼리를 작성해 보세요.
-- 1
SELECT count(*) FROM student
WHERE score > 80;
-- 2
SELECT name FROM student
ORDER BY score DESC LIMIT 1;
-- 3
SELECT grade, avg(score) FROM student
GROUP BY grade;