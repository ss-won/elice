DESC score;

-- 짜장면을 받을 수 있는 학생을 조회하는 쿼리를 작성해주세요.
SELECT * from score
WHERE korean=100 or english=100 or math=100;

-- 과자를 받을 수 있는 학생을 조회하는 쿼리를 작성해주세요.
SELECT * from score
WHERE (korean BETWEEN 70 and 95) and (english BETWEEN 70 and 95) and (math BETWEEN 70 and 95);