-- =====================================
-- SETUP: Sample Tables and Data
-- =====================================

-- Sales table
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    store_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL
);

INSERT INTO sales (store_id, product_id, amount) VALUES
(1, 101, 20000),
(1, 102, 30000),
(2, 101, 40000),
(2, 103, 60000),
(3, 104, 120000),
(3, 105, 80000);

-- Orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL
);

INSERT INTO orders (customer_id) VALUES
(1), (1), (1), (2), (2), (2), (2), (3), (3), (4), (4), (4), (4), (4), (4);

-- Employees table
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    salary INTEGER NOT NULL,
    hire_date DATE NOT NULL
);

INSERT INTO employees (name, department_id, salary, hire_date) VALUES
('Alice', 10, 80000, '2019-04-15'),
('Bob', 20, 55000, '2021-05-10'),
('Charlie', 10, 90000, '2022-07-22'),
('Diana', 30, 60000, '2020-01-30'),
('Eve', 20, 51000, '2018-10-10'),
('Frank', 10, 95000, '2023-03-01');

-- =====================================
-- 1. GROUP BY without HAVING
-- =====================================
SELECT store_id, SUM(amount) AS total_sales
FROM sales
GROUP BY store_id;

-- =====================================
-- 2. GROUP BY with HAVING (sales > $100,000)
-- =====================================
SELECT store_id, SUM(amount) AS total_sales
FROM sales
GROUP BY store_id
HAVING SUM(amount) > 100000;

-- =====================================
-- 3. GROUP BY with Multiple Columns
-- =====================================
SELECT store_id, product_id, SUM(amount) AS total_sales
FROM sales
GROUP BY store_id, product_id;

-- =====================================
-- 4. GROUP BY with COUNT() – Orders per Customer
-- =====================================
SELECT customer_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id;

-- =====================================
-- 5. GROUP BY with AVG() – Avg Salary per Department
-- =====================================
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id;

-- =====================================
-- 6. GROUP BY with HAVING and SUM() – Total Salary > $500,000
-- =====================================
SELECT department_id, SUM(salary) AS total_salary
FROM employees
GROUP BY department_id
HAVING SUM(salary) > 500000;

-- =====================================
-- 7. GROUP BY with HAVING and COUNT() – Customers with > 5 Orders
-- =====================================
SELECT customer_id, COUNT(order_id) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 5;
