CREATE TABLE `tb_KickboardRental` (
  `pk_customer_id` varchar(15),
  `rental_date` varchar(20),
  `customer_name` varchar(20),
  `customer_tel` varchar(15),
  `kickboard_id` varchar(5),
  `kickboard_kind` varchar(5),
  `kickboard_image` varchar(50),
  `kickboard_year` int,
  
-- 지시사항 1번을 참고하여 유일키를 설정하세요.
  PRIMARY KEY(`pk_customer_id`)
   
  
);
DESC tb_KickboardRental 