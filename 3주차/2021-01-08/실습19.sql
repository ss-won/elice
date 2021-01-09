-- salaries 테이블에서 직원 번호와 한 직원의 평균 급여를 중복없이 출력해보세요.
SELECT DISTINCT emp_no, (
SELECT AVG(salary) FROM salaries AS A WHERE A.emp_no = B.emp_no) AS avg_salary
FROM salaries AS B;