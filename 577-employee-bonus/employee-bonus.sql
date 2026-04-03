# Write your MySQL query statement below
SELECT
Employee.name,
Bonus.bonus
FROM 
Employee LEFT OUTER JOIN Bonus on Employee.empId = Bonus.empID
WHERE Bonus.bonus < 1000 OR Bonus.bonus IS NULL;;
