-- 각 부서별 나이가 제일 많은 사원을 조회하는 쿼리를 작성해주세요.
SELECT * FROM emp
WHERE birthdate IN(
SELECT MIN(birthdate) FROM emp
GROUP BY deptno
);