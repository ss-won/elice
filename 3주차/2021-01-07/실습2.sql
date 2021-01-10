CREATE TABLE `tb_KickboardRental` (
  `pk_rental_date` varchar(20),
  `pk_customer_id` varchar(15),
  `customer_name` varchar(20),
  `customer_tel` varchar(15),
  `kickboard_id` varchar(5),
  `kickboard_kind` varchar(5),
  `kickboard_image` varchar(50),
  `kickboard_year` int,
  
-- 지시사항 1번을 참고하여 복합키를 설정하세요.
   PRIMARY KEY(`pk_customer_id`, `pk_rental_date`)
   
   
);
DESC tb_KickboardRental