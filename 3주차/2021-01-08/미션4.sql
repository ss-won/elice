-- 1. 경민이보다 중간고사 수학점수를 높거나 같게 받은 학생들을 조회해 주세요.
/* SELECT * FROM middle_test;
SELECT * FROM students; */

SELECT * FROM middle_test AS m
INNER JOIN students AS s
ON m.student_id = s.student_id
WHERE math >= (SELECT math FROM middle_test WHERE student_id=10504);