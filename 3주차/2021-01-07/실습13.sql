CREATE TABLE `tb_KickboardRental` (
  `pk_rental_date` varchar(20),
  `fk_pk_customer_id` varchar(15),
  `fk_kickboard_id` varchar(5),

  PRIMARY KEY (`pk_rental_date`, `fk_pk_customer_id`),
  FOREIGN KEY (`fk_pk_customer_id`) REFERENCES `tb_CustomerInfo` (`pk_customer_id`),

-- 지시사항 1번을 참고하여 ON DELETE 옵션을 추가하세요.
  FOREIGN KEY (`fk_kickboard_id`) REFERENCES `tb_KickboardInfo` (`pk_kickboard_id`) ON DELETE SET NULL
  
  
  
);