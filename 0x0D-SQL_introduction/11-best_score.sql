-- Lists all records in the second_table with a score >= 10 in my MySQL server.
-- Order records by descending score order.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;