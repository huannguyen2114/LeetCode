/* Write your T-SQL query statement below */
SELECT C.id FROM Weather C, Weather P WHERE  DATEDIFF(DAY, P.recordDate, C.recordDate) =1 AND C.temperature > P.temperature ;