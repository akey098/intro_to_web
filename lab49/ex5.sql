-- Begin transaction
BEGIN;

-- Insert a new record
INSERT INTO users (name, email, age) VALUES ('David Tran', 'david@example.com', 28);

-- Update an existing record
UPDATE users
SET age = 29
WHERE email = 'david@example.com';

-- Delete a record
DELETE FROM users
WHERE name = 'Bob Jones';

-- Rollback to undo all changes
ROLLBACK;

-- Verify rollback was successful
SELECT * FROM users;
