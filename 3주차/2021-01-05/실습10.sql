-- 문제의 조건에 맞는 직원을을 출력합니다.
SELECT * from employees
WHERE (first_name='Chirstian' or first_name='Georgi') and gender='M' and NOT (hire_date ='1986-06-26');
