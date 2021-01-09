-- 대출,반납에 대한 정보를 user 테이블과 연결해 조회해 봅시다.
-- 대신 rental 테이블이 중심이 되도록 조회해 봅시다.
SELECT * FROM rental AS r
LEFT JOIN user AS u
ON r.user_id = u.id;