-- Create the users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INTEGER NOT NULL
);

-- Insert records
INSERT INTO users (name, email, age) VALUES
('Alice Smith', 'alice@example.com', 25),
('Bob Jones', 'bob@example.com', 30),
('Charlie Lee', 'charlie@example.com', 35);

-- Verify
SELECT * FROM users;
