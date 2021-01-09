-- 연봉에 대한 정보를 employees 테이블과 연결해 조회해 봅시다.
SELECT * FROM salaries AS s
INNER JOIN employees AS e
ON s.emp_no = e.emp_no