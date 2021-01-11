SELECT * FROM emp;
-- MANAGER 업무를 가진 사원 중 제일 높은 급여를 받는 사원보다 높은 급여를 받는 사원을 조회하는 쿼리를 작성해주세요.
SELECT * FROM emp
WHERE sal > ALL(SELECT sal FROM emp 
WHERE job='MANAGER')

-- ALL은 모든 데이터에 대해 &&연산을 하기 때문에, 원하는 데이터 중 최댓값을 