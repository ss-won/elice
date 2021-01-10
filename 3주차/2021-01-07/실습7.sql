-- 지시사항 1번을 참고하여 View를 생성하세요.
CREATE VIEW v_KickboardInfoForCustomer AS
SELECT pk_kickboard_id, kickboard_kind, kickboard_image
FROM tb_KickboardInfo;

SELECT * FROM v_KickboardInfoForCustomer;