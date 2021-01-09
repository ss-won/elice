SELECT * FROM emp;
-- 사원 번호가 7인 사원보다 나이가 어린 사원의 모든 컬럼을 조회 하는 쿼리를 작성하세요.
SELECT * FROM emp
WHERE birthdate > (SELECT birthdate FROM emp WHERE empnum = 7);