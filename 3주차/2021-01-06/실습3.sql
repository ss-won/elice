-- 아래에 hire_date에 7이 들어가는 직원을 조회하는 쿼리를 작성해주세요.
-- 숫자인것처럼 보이지만, date타입은 문자열로 인식되기 때문에 다음과 같이 LIKE로 질의 가능
-- desc employees;
SELECT * FROM employees
WHERE hire_date LIKE '%7%';