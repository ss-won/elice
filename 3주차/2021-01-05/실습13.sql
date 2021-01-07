-- 책들의 정보가 담긴 테이블의 구조를 출력합니다. 수정하실 필요는 없습니다.
DESC book;

-- 해당하는 작가가 쓴 책만 골라서 출력합니다.
SELECT * from book
WHERE author IN ('William Shakespeare','John Ronald Reuel Tolkien','Joanne Kathleen Rowling');