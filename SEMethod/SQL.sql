SELECT
  Calon_ID,
  SUM(pemilih) AS total_s,
  COUNT(Calon_ID) AS COUNT
FROM 
  Table_Suara
GROUP BY
  USER_ID