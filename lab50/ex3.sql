-- First name starts with 'A'
SELECT * FROM employees
WHERE first_name LIKE 'A%';

-- Last name contains 'son'
SELECT * FROM employees
WHERE last_name LIKE '%son%';

-- First name ends with 'e'
SELECT * FROM employees
WHERE first_name LIKE '%e';
