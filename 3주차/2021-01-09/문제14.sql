-- 아래에 쿼리를 작성해 보세요.
SELECT gender, avg(height), avg(weight) FROM student GROUP BY gender;
SELECT weight FROM student WHERE gender ='M' ORDER BY height DESC LIMIT 1;
SELECT weight FROM student WHERE gender ='F' ORDER BY height LIMIT 1;