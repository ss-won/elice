-- 테이블의 구조를 출력하는 쿼리입니다. 실행 버튼을 눌러보시면 테이블의 구조를 알 수 있습니다.
DESC book;

-- Joanne Kathleen Rowling작가의 책만 골라서 조회하는 쿼리를 작성해주세요.
SELECT * from book
Where author="Joanne Kathleen Rowling";