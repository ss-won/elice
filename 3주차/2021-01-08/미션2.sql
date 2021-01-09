-- 지시사항을 만족하는 쿼리를 작성해보세요.

SELECT name, SUM(amount) FROM sale
GROUP BY name HAVING SUM(revenue) >= 50000;