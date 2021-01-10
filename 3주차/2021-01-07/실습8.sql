-- 지시사항 1번을 참고하여 코드를 작성하세요.
CREATE VIEW v_KickboardInfoForAnalysis AS
SELECT kr.pk_rental_date, ki.kickboard_kind, ki.kickboard_year
FROM tb_KickboardInfo AS ki, tb_KickboardRental as kr
WHERE kr.fk_kickboard_id = ki.pk_kickboard_id;

SELECT * FROM v_KickboardInfoForAnalysis;