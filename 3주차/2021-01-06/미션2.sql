-- 아래에 문제 설명대로 수정해 봅시다.
UPDATE product SET stock=0 WHERE id=1; 
UPDATE product SET selling_price=800 WHERE id=2;
UPDATE product SET stock=50 WHERE id=3;
DELETE FROM product WHERE id=4;

-- 수정된 product테이블 전체를 조회합니다. 만약 product를 수정하지 않았다면 수정되지 않은 값이 조회됩니다.
select * from product;