# Write your MySQL query statement below
SELECT E.name  AS Employee
FROM  Employee e 
JOIN Employee m 
 ON e.managerId = m.id
WHERE e.salary > m.salary;