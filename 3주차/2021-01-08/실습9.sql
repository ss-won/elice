-- 연봉에 대한 정보를 employees 테이블과 연결해 조회하되 salaries 테이블을 중심으로 조회해보세요.
SELECT * FROM salaries AS s
LEFT JOIN employees AS e
ON s.emp_no = e.emp_no;