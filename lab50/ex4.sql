-- Salaries between 50,000 and 70,000
SELECT * FROM employees
WHERE salary BETWEEN 50000 AND 70000;

-- Hired between 2019 and 2021
SELECT * FROM employees
WHERE hire_date BETWEEN '2019-01-01' AND '2021-12-31';
