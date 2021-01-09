-- salaries 테이블에서 emp_no과 직원별로 연봉을 받은 횟수를 조회해보세요.
SELECT emp_no, COUNT(*) FROM salaries
GROUP BY emp_no;