-- 지시사항 1번을 참고하여 DEFAULT 속성을 추가하세요.
CREATE TABLE `tb_KickboardInfo` (
  `pk_kickboard_id` varchar(5),
  `kickboard_kind` varchar(5) DEFAULT 'A',
  `kickboard_image` varchar(50) DEFAULT 'https://...',
  `kickboard_year` int DEFAULT 2020,
  PRIMARY KEY (`pk_kickboard_id`)
);

INSERT INTO tb_KickboardInfo (pk_kickboard_id) VALUES ('E04');
SELECT * FROM tb_KickboardInfo