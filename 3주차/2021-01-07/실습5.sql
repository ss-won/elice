CREATE TABLE `tb_CustomerInfo_2NF` (

  `pk_customer_id` varchar(15),
  `customer_name` varchar(20),
  `customer_tel` varchar(15),
  
-- 지시사항 1번을 참고하여 속성을 추가해주세요.
  PRIMARY KEY(`pk_customer_id`)
  
  
);



CREATE TABLE `tb_KickboardRental_2NF` (

  `pk_rental_date` varchar(20),
  `fk_pk_customer_id` varchar(15),
  `kickboard_id` varchar(5),
  `kickboard_kind` varchar(5),
  `kickboard_image` varchar(50),
  `kickboard_year` int,
  
-- 지시사항 2번을 참고하여 속성을 추가해주세요.
  PRIMARY KEY(`pk_rental_date`, `fk_pk_customer_id`),
  FOREIGN KEY(`fk_pk_customer_id`) REFERENCES `tb_CustomerInfo_2NF`(`pk_customer_id`)
  
  
);

INSERT INTO tb_CustomerInfo_2NF VALUES ('elice_rabbit', '엘리스 토끼', '010-1111-2222');
INSERT INTO tb_CustomerInfo_2NF VALUES ('hatseller', '모자장수', '010-2222-3333');

INSERT INTO tb_KickboardRental_2NF VALUES ('2020-10-01 11:00', 'elice_rabbit', 'E01', 'A', 'http://...', 2019);
INSERT INTO tb_KickboardRental_2NF VALUES ('2020-10-02 12:00', 'elice_rabbit', 'E02', 'B', 'http://...', 2020);
INSERT INTO tb_KickboardRental_2NF VALUES ('2020-10-02 12:00', 'hatseller', 'E01', 'A', 'http://...', 2019);
INSERT INTO tb_KickboardRental_2NF VALUES ('2020-10-02 14:00', 'hatseller','E03', 'A', 'http://...', 2019);

SELECT * FROM tb_CustomerInfo_2NF;
SELECT * FROM tb_KickboardRental_2NF
