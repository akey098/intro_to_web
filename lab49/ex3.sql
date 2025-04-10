-- Remove a user by email
DELETE FROM users
WHERE email = 'charlie@example.com';

-- Delete users above a certain age
DELETE FROM users
WHERE age > 30;

-- Verify
SELECT * FROM users;
