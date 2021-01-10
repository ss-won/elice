-- 지시사항 1번을 참고하여 NOT NULL 속성을 추가하세요.
CREATE TABLE `tb_CustomerInfo` (
  `pk_customer_id` varchar(15),
  `customer_name` varchar(20) NOT NULL,
  `customer_tel` varchar(15) NOT NULL,
  PRIMARY KEY (`pk_customer_id`)
);

-- 지시사항 2번을 참고하여 NOT NULL 속성을 추가하세요.
CREATE TABLE `tb_KickboardInfo` (
  `pk_kickboard_id` varchar(5),
  `kickboard_kind` varchar(5) NOT NULL,
  `kickboard_image` varchar(50) NOT NULL,
  `kickboard_year` int NOT NULL,
  PRIMARY KEY (`pk_kickboard_id`)
);

DESC tb_CustomerInfo;
DESC tb_KickboardInfo;