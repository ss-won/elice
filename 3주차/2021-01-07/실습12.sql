CREATE TABLE `tb_KickboardRental` (
  `pk_rental_date` varchar(20),
  `fk_pk_customer_id` varchar(15),
  `fk_kickboard_id` varchar(5),

  PRIMARY KEY (`pk_rental_date`, `fk_pk_customer_id`),
  FOREIGN KEY (`fk_kickboard_id`) REFERENCES `tb_KickboardInfo` (`pk_kickboard_id`),

-- 지시사항 1번을 참고하여 ON UPDATE 옵션을 추가하세요.
  FOREIGN KEY (`fk_pk_customer_id`) REFERENCES `tb_CustomerInfo` (`pk_customer_id`) ON UPDATE CASCADE
  
);

-- 대여 테이블에 데이터 추가
INSERT INTO tb_KickboardRental VALUES ('2020-10-01 11:00', 'elice_rabbit', 'E01');
-- elice_rabbit의 아이디 변경
UPDATE tb_CustomerInfo SET pk_customer_id = 'elice_rabbit2' WHERE pk_customer_id = 'elice_rabbit';
--출력을 통해 아이디가 변경되었는지 확인
SELECT * FROM tb_KickboardRental;
