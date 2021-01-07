-- 학생들의 성적이 담겨있는 테이블의 구조를 조회합니다. 수정하실 필요는 없습니다.
DESC grade;

-- 학생들의 성적의 평균을 조회합니다.
SELECT AVG(korean), AVG(english), AVG(math) FROM grade;