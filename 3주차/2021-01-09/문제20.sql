-- 각 물건별로 몇개가 팔렸는지 정리해 출력해 봅시다.
-- 이때 한번만 팔린 물건은 출력하지 않습니다.
SELECT product_id, sum(amount) FROM sale
GROUP BY product_id HAVING count(product_id) > 1;
