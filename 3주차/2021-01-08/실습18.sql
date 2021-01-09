-- salaries 테이블에서 from_date가 2000-12-31 이전인 사람들의 급여 중 하나의 급여 보다 더 적은 급여를 받은 직원의 급여 정보를 모두 출력해보세요.
SELECT * FROM salaries
WHERE salary < ANY(
SELECT salary FROM salaries
WHERE from_date < '2000-12-31'
);

-- salaries 테이블에서 from_date가 2000-12-31 이전인 사람들의 급여 중 모든 급여보다 적은 급여를 받은 직원의 급여 정보를 모두 출력해보세요.
SELECT * FROM salaries
WHERE salary < ALL(
SELECT salary FROM salaries
WHERE from_date < '2000-12-31'
);
