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


## Concat
 1) Select Concat(brand1, brand2, brand3) as paired_value

## CASE
1) Select Case when brand1 < brand2 then concat(brand1,brand2, brand3)
                when brand1 > brand2 then concat(brand2,brand1, brand3)
                else concat(brand1, brand2, brand3)
                end as Column_name


## OFFSET : It is not good as the query will run completely and just before it returns the output it will remove those many rows
It will remove the first N records

For Eg: Problem Return the Nth highest value without using subquery or windows function
-- Find the 2nd highest Amount
select
from orders
order by amount desc
limit 1 offset 1; -- It will eliminate the 1st record with the help of OFFSET and return the record from th elist based on the limit.

## DISTINCT ON : Return one row per group without windows function

For Eg: Find the latest order for each customer
select distinct on (customer_name)
from orders
order by customer_name, order_date desc

## RETURNING : Return the Modified data from DML operation

For Eg: Return the modified records

BEGIN;  -- Use BEGIN, so your transaction doesn't autocommit, the changes does not get save dto the databse directly, I have an option to rollback if I want later.

UPDATE orders
SET category = 'Premium Electronics'
WHERE category = 'Electronics' AND amount > 150
RETURNING order_id, customer_name, amount

ROLLBACK;

## Range Overlap with && and daterange function : Overlap function detects overlapping dates in ONE operator

For Eg: The manager needs to know if any two salespeople have overlapping approved leave, because someone always has to  be covering the floor

SELECT 
    a.salesperson as salesperson_1, a.leave_start as start_1, a.leave_end as end_1,
    b.salesperson as salesperson_2, a.leave_start as start_2, a.leave_end as end_2
from staff_leave a
join staff_leave b
on a.leave_id < b.leave_id
AND a.salesperson <> b.salesperson
AND daterange(a.leave_start, a.leave_end,'[]') && daterange(b.leave_start, b.leave_end,'[]')
ORDER BY a.leave_start


## GENERATE_SERIES : Find gaps using GENERATE_SERIES(start, stop, step)

For Eg: Return days with no data

with cte_date_range as (
    SELECT generate_series('2026-01-01'::date, '2026-01-31'::date, '1 day':: interval)::date as calender_date
)
select ds.calender_date
from cte_date_range ds
left join orders o
on o.order_date = ds.calender_date
where o.order_id is null
order by ds.calender_date;