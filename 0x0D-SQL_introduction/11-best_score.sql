--lists all records with score >=10
--records are ordered in descending order
SELECT `score`, `name`
FROM `second_name`
WHERE `score` >=10
ORDER BY `score` DESC;

