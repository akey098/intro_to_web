-- Update age for a user
UPDATE users
SET age = 26
WHERE name = 'Alice Smith';

-- Change email address
UPDATE users
SET email = 'robert.jones@example.com'
WHERE name = 'Bob Jones';

-- Verify
SELECT * FROM users;
