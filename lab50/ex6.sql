-- Sorted by first name A–Z
SELECT * FROM employees
ORDER BY first_name ASC;

-- Sorted by salary high to low
SELECT * FROM employees
ORDER BY salary DESC;

-- Sorted by department A–Z, then salary high to low
SELECT * FROM employees
ORDER BY department ASC, salary DESC;
