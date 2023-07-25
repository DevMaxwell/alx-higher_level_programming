-- Lists all records of the table; second_table whhere name value is not empty string.
-- Order records in descending score order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC