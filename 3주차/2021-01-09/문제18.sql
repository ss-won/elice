-- 아래에 미션을 수행하는 쿼리를 작성해 보세요.
SELECT* FROM product
WHERE expiration_date < '2019-05-01';

SELECT sum(stock) FROM product
WHERE expiration_date < '2019-05-01';