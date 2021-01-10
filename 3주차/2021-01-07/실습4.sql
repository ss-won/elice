-- 현재 tb_CustomerInfo 테이블의 상태를 출력하는 코드입니다.
SELECT * FROM tb_CustomerInfo;


-- 지시사항 1번을 참고하여 1차 정규화에 맞춰 데이터를 추가하세요.

DELETE FROM tb_CustomerInfo;

INSERT INTO tb_CustomerInfo VALUES('elice_rabbit');
INSERT INTO tb_CustomerInfo VALUES('hatseller');
INSERT INTO tb_CustomerInfo VALUES('dodo_bird');

SELECT * FROM tb_CustomerInfo;