SQL Concepts:
Let's take an employee table with columns - empid, emp_name, dept_name, salary
We want to find the max salary of an employee from each department -
# SQL
select dept_name, max(salary) as max_salary 
from employee
group by dept_name;

 ## Windows Function - 
1) Aggregate Function:
# Eg: Get the maximum salary of an employee from each department
select
max(salary) over(partition by dept_name) as max_salary
from employee e;

2) ROW_NUMBER: It assigns a unique number to each row: --1,2,3,4 
# Eg: Get a unique row number for each row
-- Find the first 2 employee who joined each department 
select * from (
select 
row_number() over(partition by dept_name order by empid asc) as rn
from employee e) x
where x.rn < 3;

3) RANK: If it finds duplicate value it will assign same rank, and skip the value for the next element : --1,2,2,4
# Eg: Fetch top 3 employees from each department earning max salary
select * from (
select
rank() over(partition by dept_name order by salary desc) as rnk
from employee e) x
where x.rnk < 4;


4) DENSE_RANK: If it finds duplicate value it will assign same rank, and it will not skip the value for the next element : --1,2,2,3
# Eg: Fetch top 3 employees from each department earning max salary
select * from (
select
dense_rank() over(partition by dept_name order by salary desc) as rnk
from employee e) x
where x.rnk < 4;

5) LAG: LAG(column name, how much previous record, default value to display)
# Eg: Fetch a query to display if the salary of an employee is higher, lower or equal to the previous employee
select
lag(salary,2,0) over(partition by dept_name order by empid) as prev_salary
from employee e;

# Eg: Display Higher, lower or equal compared to previous employee

select e.*,
lag(salary) over(partition by dept_name oder by empid) as prev_emp_salary,
case when e.salary > lag(salary) over(partition by dept_name order by empid) then 'Higher than previous employee'
e.salary < lag(salary) over(partition by dept_name order by empid) then 'Lower than previous employee'
e.salary = lag(salary) over(partition by dept_name order by empid) then 'Equal than previous employee'
end sal_range
from employee e;

6) LEAD: LAG(column name, how much following record, default value to display)
# Eg: Fetch a query to display if the salary of an employee is higher, lower or equal to the following employee
select
lead(salary,2,0) over(partition by dept_name order by empid) as next_salary
from employee e;


## MySQL Date
1) Current Date : CURDATE()

2) Adding and Subtracting Time
Select DATE_ADD(order_date, INTERVAL 7 DAY); -- Add 7 days
Select DATE_SUB(order_date, INTERVAL 1 MONTH); -- Subtract 1 month

3) Calculating the difference between Two Dates
Select DATEDIFF('2026-02-04','2027-03-05');

4) Extracting Parts of Date
Select YEAR(order_date), MONTH(order_date), DAY(order_date)
Select EXTRACT(YEAR from order_date)

5) Custom Date Formatting
select DATE_FORMAT(NOW(),'%W, %M %e, %Y') ---(e.g., Friday, October 2, 2026)
