CREATE TABLE `tb_KickboardRental` (
  `pk_rental_date` varchar(20),
  `fk_pk_customer_id` varchar(15),
  `customer_name` varchar(20),
  `customer_tel` varchar(15),
  `kickboard_id` varchar(5),
  `kickboard_kind` varchar(5),
  `kickboard_image` varchar(50),
  `kickboard_year` int,
   PRIMARY KEY (`pk_rental_date`, `fk_pk_customer_id`),
  
-- 지시사항 1번을 참고하여 외래키를 설정하세요.
   FOREIGN KEY (`fk_pk_customer_id`) REFERENCES `tb_CustomerInfo`(`pk_customer_id`)
);

-- 지시사항 2번을 참고하여 도도새에 대한 고객 정보를 추가하세요.
INSERT INTO tb_CustomerInfo VALUES ('dodo_bird');
INSERT INTO tb_KickboardRental VALUES ('2020-10-01 11:00', 'dodo_bird', '도도새', '010-3333-4444', 'E01', 'A','https://...', '2019');

SELECT * FROM tb_CustomerInfo;
SELECT * FROM tb_KickboardRental;
