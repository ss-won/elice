-- 아래에 쿼리를 작성해 보세요.
ALTER TABLE student ADD score float;
UPDATE student SET score = ((midterm+final)*4.5)/200;
SELECT name, score FROM student;