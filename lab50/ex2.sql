-- Employees with a salary greater than 60,000
SELECT * FROM employees
WHERE salary > 60000;

-- Employees hired after January 1, 2020
SELECT * FROM employees
WHERE hire_date > '2020-01-01';

-- Employees in HR or Finance department
SELECT * FROM employees
WHERE department = 'HR' OR department = 'Finance';
