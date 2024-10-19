-- 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회
-- 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시
-- 취소되지 않은 -> 예약 취소 여부 OR APNT_CNCL_YMD IS NULL

SELECT
    apnt_no,
    pt_name,
    a.pt_no,
    a.mcdp_cd,
    dr_name,
    apnt_ymd
FROM APPOINTMENT a
    LEFT JOIN PATIENT p
        ON p.pt_no = a.pt_no
    LEFT JOIN DOCTOR d
        ON d.dr_id = a.mddr_id
WHERE a.apnt_ymd BETWEEN '2022-04-13 00:00:00' AND '2022-04-13 23:59:59'
    AND a.mcdp_cd = 'CS'
    AND a.apnt_cncl_yn = 'N'
ORDER BY apnt_ymd