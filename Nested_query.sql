/*
Given two tables Salesperson and Orders with following columns:

Salesperson:  ID, Name, Age, Salary
Orders:  Number, order_date, cust_id, salesperson_id, Amount

Write a SQL query that retrieves the names of all salespeople that have more than 1 
order from the tables above. You can assume that each salesperson only has one ID.
*/
Select name from Salesperson join
(Select salesperson_id, count(salesperson_id) as cnt from Orders group by salesperson_id)
on (ID=salesperson_id)
where cnt>1