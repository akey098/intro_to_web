-- Employees in IT or HR
SELECT * FROM employees
WHERE department IN ('IT', 'HR');

-- Employees with specific salary values
SELECT * FROM employees
WHERE salary IN (48000, 65000, 72000);
