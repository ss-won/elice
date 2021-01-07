-- 잃어버린 책 2권을 book 테이블에서 삭제하여 봅시다.
DELETE FROM book 
WHERE title="Harry Potter and the Philosopher's Stone" or title="The Lord of the Rings";


-- 전체 책의 정보와 회원정보를 조회합니다. 수정하실 필요는 없습니다.
SELECT * FROM book;