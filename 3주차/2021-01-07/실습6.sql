CREATE TABLE `tb_KickboardInfo_3NF` (

  `pk_kickboard_id` varchar(5),
  `kickboard_kind` varchar(5),
  `kickboard_image` varchar(50),
  `kickboard_year` int,
  
-- 지시사항 1번을 참고하여 속성을 추가해주세요.
  PRIMARY KEY(`pk_kickboard_id`)


);


CREATE TABLE `tb_KickboardRental_3NF` (

  `pk_rental_date` varchar(20),
  `fk_pk_customer_id` varchar(15),
  `fk_kickboard_id` varchar(5),
  
-- 지시사항 2번을 참고하여 속성을 추가해주세요.
  PRIMARY KEY(`pk_rental_date`, `fk_pk_customer_id`),
  FOREIGN KEY(`fk_pk_customer_id`) REFERENCES
  `tb_CustomerInfo`(`pk_customer_id`),
  FOREIGN KEY(`fk_kickboard_id`) REFERENCES `tb_KickboardInfo_3NF`(`pk_kickboard_id`)

);

INSERT INTO tb_KickboardInfo_3NF VALUES ('E01', 'A', 'https://...', 2019);
INSERT INTO tb_KickboardInfo_3NF VALUES ('E02', 'B', 'https://...', 2020);
INSERT INTO tb_KickboardInfo_3NF VALUES ('E03', 'A', 'https://...', 2019);

INSERT INTO tb_KickboardRental_3NF VALUES ('2020-10-01 11:00', 'elice_rabbit', 'E01');
INSERT INTO tb_KickboardRental_3NF VALUES ('2020-10-02 12:00', 'elice_rabbit', 'E02');
INSERT INTO tb_KickboardRental_3NF VALUES ('2020-10-02 12:00', 'hatseller', 'E01');
INSERT INTO tb_KickboardRental_3NF VALUES ('2020-10-02 14:00', 'hatseller','E03');

SELECT * FROM tb_KickboardInfo_3NF;
SELECT * FROM tb_KickboardRental_3NF