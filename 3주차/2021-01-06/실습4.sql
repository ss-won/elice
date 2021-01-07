--- book 테이블의 구조를 조회합니다. 수정하실 필요는 없습니다.
DESC book;

-- book 테이블의 내용을 조회해 봅시다. 이때 책 제목을 기준으로 오름차순으로 조회해 봅시다.
-- default값이 오름차순(ASC)
SELECT * FROM book
ORDER BY title;
