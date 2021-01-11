-- 판매기록을 product 테이블과 연결해 출력해 봅시다.
-- 이때 product테이블이 중심이 되도록 해 봅시다.
SELECT * FROM sale AS s
RIGHT JOIN product AS p
ON s.product_id = p.id;